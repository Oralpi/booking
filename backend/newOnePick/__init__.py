from flask import Flask, jsonify, request as req
from newOnePick.DBConnection.mysql import pymsl as pym
import requests as reqs
from flask_cors import CORS
import math
import datetime as dt
import json
from newOnePick.DBConnection.SetBasicXmlInfo import SetBasicXmlInfoVo as sbxivo
import xmltodict as xtd
import pymysql as pyms

app = Flask(__name__)
app.debug = True

CORS(app, resources={r'/*': {'origins': '*'}})


def HotelInfo():
    url = ''
    authId = ''
    authKey = ''

    sbx = sbxivo(url, authId, authKey)
    return sbx
# @app.route('/hotel-info', methods=['POST'])
# def hotelInfo():
#     # db 객체 정보를 호출함
#     db = sq()
#     dbs = db.getDB()
#     # cursor 객체를 호출 (cursor) db를 제어 시킬 수 있는 모듈 객체
#     cursor = dbs.cursor()
#     sql = 'select ham_seq_no, ham_property_id, ham_city_code from hs_accommodation_master'

#     cursor.execute(sql)

#     data = list(cursor.fetchall())
#     js = {
#         "hotel": []
#     }
#     for no, id, code in data:
#         index = 0
#         image = 'select image.hai_image_url from hs_accommodation_images as image left join hs_accommodation_master as master on image.ham_seq_no = %s'
#         cursor.execute(image, [no])

#         images = list(cursor.fetchall())
#         for image in images:
#             index += 1
#             if index == 1:
#                 js['hotel'].append(
#                     {"property_id": id, "city": code, "img_url": image[0]})
#             break
#     return jsonify(js)


# @app.route('/hotelStory-list', methods=['POST'])
# def hotelStory():
#     db = sq()
#     length = 'select count(*) from hs_accommodation_master'
#     sql = 'select ham_seq_no, ham_property_id, ham_city_code, ham_star_rating, ham_property_name, ham_address, ham_property_desc from hs_accommodation_master limit 10 offset %s'
#     cur = db.getDB().cursor()
#     start = int(req.form.get('start'))

#     cur.execute(sql, [start])

#     master = list(cur.fetchall())

#     cur.execute(length)

#     currentLength = len(master)
#     lengths = cur.fetchone()
#     paging = []
#     pageList = []
#     for page in range(1, (math.ceil((lengths[0] / 10)) + 1)):
#         pageList.append(page)
#         if (page % 10) == 0:
#             # print("첫번째: ", (page % 10) == 0)
#             paging.append(pageList)
#             pageList = []
#         elif page == ((math.ceil((lengths[0] / 10)))):
#             # print("마지막: ", page == ((math.ceil((lengths[0] / 10)) + 1)))
#             paging.append(pageList)
#     js = {
#         "hotelStory": [],
#         "lens": lengths[0],
#         "currentLength": currentLength,
#         "pageList": paging,
#         "pagelens": len(paging)
#     }

#     for no, id, code, rating, name, addr, desc in master:
#         index = 0
#         img_sql = 'select image.hai_image_url from hs_accommodation_images as image inner join hs_accommodation_master as master on image.ham_seq_no = %s'

#         cur.execute(img_sql, [no])

#         images = list(cur.fetchall())
#         for image in images:
#             index += 1

#             if index == 1:
#                 js['hotelStory'].append({
#                     "id": id,
#                     "code": code,
#                     "rating": rating,
#                     "name": name,
#                     "addr": addr,
#                     "desc": desc,
#                     "image": image[0]
#                 })

#     return jsonify(js)

@app.route('/hotel-story', methods=['POST'])
def hotel_story():
    start = str(req.form.get('start'))
    search_word = str(req.form.get('search_word'))
    db = pym()
    lens = "select count(*) from hs_accommodation_master where instr(ham_address, '%s')" % (search_word)
    sql = "select ham_seq_no, ham_property_id, ham_city_code, ham_star_rating, ham_property_name, ham_address, ham_property_desc from hs_accommodation_master where instr(ham_address, '%s') limit 10 offset %s" % (
        search_word, start)
    # cur = db.getDB().cursor()
    master = []
    lengths = 0

    # cur.execute(sql)
    master = db.execute_selectAll(sql)

    # master = list(cur.fetchall())

    # cur.execute(lens)

    lengths = db.execute_selectOne(lens)[0]

    paging = []
    pageList = []

    for page in range(1, (math.ceil(lengths / 10) + 1)):
        pageList.append(page)

        if(page % 10) == 0:
            paging.append(pageList)

            pageList = []
        elif page == math.ceil(lengths / 10):
            paging.append(pageList)

    js = {
        "hotelStory": [],
        "length": lengths,
        "pageList": paging,
        "pagelens": len(paging)
    }

    for no, id, code, rating, name, addr, desc in master:
        index = 0
        img_sql = 'select image.hai_image_url from hs_accommodation_images as image inner join hs_accommodation_master as master on image.ham_seq_no = %s'

        # cur.execute(img_sql, [no])

        # images = list(cur.fetchall())
        images = db.execute_selectAllData(img_sql, [no])
        for image in images:
            index += 1

            if index == 1:
                js['hotelStory'].append({
                    "id": id,
                    "code": code,
                    "rating": rating,
                    "name": name,
                    "addr": addr,
                    "desc": desc,
                    "image": image[0]
                })

    return jsonify(js)


@app.route('/detail', methods=['POST'])
def detail():
    db = pym()
    id = req.form.get("id")
    sql = 'SELECT ham_seq_no, ham_city_code, ham_address, ham_homepage_url, ham_phone, ham_checkin_time, ham_checkout_time, ham_traffic_information, ham_checkin_instructions FROM hs_accommodation_master where ham_property_id = %s'
    # cur = db.getDB().cursor()

    # cur.execute(sql, [id])

    # detail = cur.fetchone()
    detail = db.execute_selectOneData(sql, [id])
    js = {
        "detail": [],
        "image": []
    }

    js['detail'].append({"city": detail[1], "address": detail[2], "url": detail[3], "phone": detail[4],
                        "checkIn": detail[5], "checkOut": detail[6], "information": detail[7], "instructions": detail[8]})

    img_sql = 'select image.hai_image_url from hs_accommodation_images as image inner join hs_accommodation_master as master on image.ham_seq_no = %s'

    # cur.execute(img_sql, [detail[0]])

    # image = list(cur.fetchall())
    image = db.execute_selectAllData(img_sql, [detail[0]])
    index = 0

    for images in image:
        js['image'].append(images)

        index += 1

        if index == 6:
            break

    return jsonify(js)


# @app.route('/search-paging', methods=['POST'])
# def search_paging():
#     start = str(req.form.get('start'))
#     search_word = str(req.form.get('search_word'))
#     db = sq()
#     lens = "select count(*) from hs_accommodation_master where instr(ham_address, '%s')" % (
#         search_word)
#     sql = "select ham_seq_no, ham_property_id, ham_city_code, ham_star_rating, ham_property_name, ham_address, ham_property_desc from hs_accommodation_master where instr(ham_address, '%s') limit 10 offset %s" % (
#         search_word, start)
#     cur = db.getDB().cursor()
#     master = []
#     lengths = 0

#     try:
#         cur.execute(sql)

#         master = list(cur.fetchall())

#         cur.execute(lens)

#         lengths = cur.fetchone()[0]
#     except py.err.DatabaseError as e:
#         print(e)

#     paging = []
#     pageList = []

#     for page in range(1, (math.ceil((lengths / 10)) + 1)):
#         pageList.append(page)

#         if (page % 10) == 0:
#             # print("첫번째: ", (page % 10) == 0)
#             paging.append(pageList)

#             pageList = []
#         elif page == ((math.ceil((lengths / 10)))):
#             # print("마지막: ", page == ((math.ceil((lengths[0] / 10)) + 1)))
#             paging.append(pageList)

#     js = {
#         "hotelStory": [],
#         "length": lengths,
#         "pageList": paging,
#         "pagelens": len(paging)
#     }

#     for no, id, code, rating, name, addr, desc in master:
#         index = 0
#         img_sql = 'select image.hai_image_url from hs_accommodation_images as image inner join hs_accommodation_master as master on image.ham_seq_no = %s'

#         cur.execute(img_sql, [no])

#         images = list(cur.fetchall())
#         for image in images:
#             index += 1

#             if index == 1:
#                 js['hotelStory'].append({
#                     "id": id,
#                     "code": code,
#                     "rating": rating,
#                     "name": name,
#                     "addr": addr,
#                     "desc": desc,
#                     "image": image[0]
#                 })

#     return jsonify(js)


# @app.route('/onda-list', methods=['POST'])
# def onda():
#     db = sq()
#     length = 'select count(*) from od_accommdation_master'
#     sql = 'select oam_seq_no, oam_id, oam_name, oam_rating, oam_address, oam_property_description from od_accommdation_master limit 10 offset %s'
#     cur = db.getDB().cursor()
#     start = int(req.form.get('start'))

#     cur.execute(sql, [start])

#     master = list(cur.fetchall())

#     cur.execute(length)

#     currentLength = len(master)
#     lengths = cur.fetchone()
#     js = {
#         "onda": [],
#         "lens": lengths[0],
#         "currentLength": currentLength
#     }

#     for no, id, name, rating, address, desc in master:
#         index = 0
#         img_sql = 'select image.oai_url from od_accommodation_images as image inner join od_accommdation_master as master on image.oam_seq_no = %s'

#         cur.execute(img_sql, [no])

#         images = cur.fetchall()

#         for image in images:
#             index += 1

#             if index == 1:
#                 js['onda'].append({
#                     "id": id,
#                     "name": name,
#                     "rating": rating,
#                     "address": address,
#                     "desc": desc,
#                     "image": image[0]
#                 })

#     return jsonify(js)

@app.route('/onda', methods=['POST'])
def onda():
    start = str(req.form.get('start'))
    search_word = str(req.form.get('search_word'))
    db = pym()
    lens = "select count(*) from od_accommdation_master where instr(oam_address, '%s')" % (search_word)
    sql = "select oam_seq_no, oam_id, oam_name, oam_rating, oam_address, oam_property_description from od_accommdation_master where instr(oam_address, '%s') limit 10 offset %s" % (
        search_word, start)
    # cur = db.getDB().cursor()
    master = []
    lengths = 0
    # cur.execute(sql)
    # master = list(cur.fetchall())
    master = db.execute_selectAll(sql)
    print(master)
    # cur.execute(lens)

    # lengths = cur.fetchone()[0]
    lengths = db.execute_selectOne(lens)[0]
    paging = []
    pageList = []

    for page in range(1, math.ceil(lengths / 10) + 1):
        pageList.append(page)

        if(page % 10) == 0:
            paging.append(pageList)

            pageList = []
        elif page == math.ceil(lengths / 10):
            paging.append(pageList)

    js = {
        "onda": [],
        "lengths": lengths,
        "pageList": paging,
        "pagelens": len(paging)
    }

    for no, id, name, rating, address, property in master:
        index = 0
        img_sql = 'select image.oai_url from od_accommodation_images as image inner join od_accommdation_master as master on image.oam_seq_no = %s'

        # cur.execute(img_sql, [no])

        # images = list(cur.fetchall())
        images = db.execute_selectAllData(img_sql, [no])

        for image in images:
            index += 1

            if index == 1:
                js['onda'].append({
                    "id": id,
                    "name": name,
                    "rating": rating,
                    "address": address,
                    "property": property,
                    "image": image[0]
                })
    return jsonify(js)


@app.route('/onda-detail', methods=['POST'])
def onda_detail():
    db = pym()
    id = req.form.get("id")
    sql = 'select oam_seq_no, oam_email, oam_phone, oam_website, oam_checkin, oam_checkout, oam_property_description, oam_reservation_description from od_accommdation_master where oam_id = %s'
    # cur = db.getDB().cursor()

    # cur.execute(sql, [id])

    # detail = cur.fetchone()
    detail = db.execute_selectOneData(sql, [id])

    # room = 'select oar_seq_no from od_accommodation_rooms where oam_seq_no = %s'

    # cur.execute(room, detail[0])

    # rooms = list(cur.fetchall())

    js = {
        "detail": [],
        "image": []
    }

    js['detail'].append({
        "email": detail[1],
        "phone": detail[2],
        "website": detail[3],
        "checkin": detail[4],
        "checkout": detail[5],
        "property": detail[6],
        "reservation": detail[7]
    })
    # for no in rooms:
    #     img_sql = 'select image.ori_url from od_room_images as image inner join od_accommodation_rooms as rooms on image.oar_seq_no = rooms.oar_seq_no where image.oar_seq_no = %s'

    #     cur.execute(img_sql, no[0])

    #     image = list(cur.fetchall())
    #     js['image'].append(image[0])
    img_sql = 'select image.ori_url from od_room_images as image inner join od_accommodation_rooms as rooms on image.oar_seq_no = rooms.oar_seq_no where image.oar_seq_no = %s'

    # cur.execute(img_sql, [detail[0]])

    # image = list(cur.fetchall())
    image = db.execute_selectAllData(img_sql, [detail[0]])
    index = 0

    for images in image:
        js['image'].append(images)

        index += 1

        if index == 6:
            break

    return jsonify(js)


@app.route('/set_OndaRoomInformation', methods=['POST'])
def set_OndaRoomInformation():
    # DB 연결 객체 호출
    db = pym()
    # mssql 문
    # SQL = "select value from saveInfo where keys = 'onda.production.url' or keys = 'onda.production.auth' or keys='onda.accommodations.url'"

    # sql 실행
    # CURSOR.execute(SQL)
    # # 실행힌 sql 결과 one_DATA 변수에 초기화

    # one_DATA = CURSOR.fetchall()

    # latedate 파라미터 값 구하기
    today = str(dt.datetime.now().date()) + ' 00:00:00'

    # url 값 sql 결과에서 분류 후 초기화

    with open('C:/Kong/booking/backend/newOnePick/DBConnection/onda_url.json', 'r', encoding='utf-8') as file_json:
        json_data = json.load(file_json)
    url = json_data['url']['production'] + \
        json_data['url']['accommodations']+'?lastdate='+today
    # URL = 'http://gds.tport.io/gds/v1_5/properties?lastdate='+today
    # 동일한 코드
    # auth 값 sql 결과에서 초기화
    AUTH = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGllbnRfa2V5IjoiY2FhNmJjMThmMTEyYjRiZjljNGQxY2FmOTFkM2FjZmRmYzdkNjc4MzFiZDU0YjMyMGVjNjQ1ZmQ5YTI1MzU5OCIsInRpbWVzdGFtcCI6MTYzNTE0NTIwMTc4OCwic2VydmljZV9pZCI6MSwidGFyZ2V0IjoiY2hhbm5lbCIsInRhcmdldF9pZCI6MTA0LCJpYXQiOjE2MzUxNDUyMDEsImV4cCI6MTY2NjY4MTIwMX0._v9AI_mToxhCQ6oj7IE6u4nca5I6mwzSpi8NWzvnW8w'
    # 헤더 Dictionnary로 초기화
    HEADERS = {
        'Accept-Charset': 'UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'authorization': AUTH
    }

    # api 데이터 불러오기
    # data = req.form.get(url, headers=HEADERS)
    data = reqs.get(url, headers=HEADERS)
    print(data)
    # api 데이터 인코딩
    data.encoding = 'UTF-8'

    ondadata = data.json()
    # print(ondadata)
    seq = 0
    for OndaMainList in ondadata['properties']:
        seq += 1
        id = OndaMainList['id']
        name = OndaMainList['name']
        vendor_id = OndaMainList['vendor_id']

        classifications = OndaMainList['classifications']
        classlist = ''
        Index = 0
        flag = False
        for key in classifications:
            if (Index < len(classifications)):
                classlist += classifications[Index]
                Index += 1
            if Index == len(classifications):
                flag = True
            if not flag:
                classlist += "::"

        rating = OndaMainList['rating']
        updated_at = OndaMainList['updated_at']
        with open('C:/Kong/booking/backend/newOnePick/DBConnection/onda_url.json', 'r', encoding='utf-8') as file_json:
            json_data = json.load(file_json)

        detailurl = json_data['url']['production'] + \
            json_data['url']['accommodationDetail']
        detailurl = detailurl.replace("{property_id}", id)
        detaildata = reqs.get(detailurl, headers=HEADERS)
        detaildata.encoding = 'UTF-8'
        detaildata = detaildata.json()
        index = 0
        for key in detaildata['property']:
            index += 1
            if index == 1:
                email = detaildata['property']['email']
                phone = detaildata['property']['phone']
                website = detaildata['property']['website']
                location = detaildata['property']['location']
                locindex = 0
                for key in location:
                    locindex += 1
                    if locindex == 1:
                        address = location['address']
                        detail = location['detail']
                        postal_code = location['postal_code']
                        latitude = location['latitude']
                        longitude = location['longitude']

                        break
                checkin = detaildata['property']['checkin']
                checkout = detaildata['property']['checkout']
                property_description = detaildata['property']['property_description']
                reservation_description = detaildata['property']['reservation_description']
                notice_description = detaildata['property']['notice_description']
                refund_description = detaildata['property']['refund_description']

                # 환불 diction 변환
                refund_percentage = detaildata['property']['refund_percentage']
                refundlist = ''
                flag = False
                percentIndex = 0
                for key in refund_percentage:
                    if (percentIndex < len(refund_percentage.keys())):
                        refundlist += list(refund_percentage.keys())[percentIndex] + ':' + str(
                            list(refund_percentage.values())[percentIndex])
                        percentIndex += 1
                    if percentIndex == len(refund_percentage.keys()):
                        flag = True
                    if not flag:
                        refundlist += "::"
                property_tags = detaildata['property']['property_tags']
                propertyTaglist = ''
                flag = False
                Index = 0
                for key in property_tags:
                    if (Index < len(property_tags)):
                        propertyTaglist += property_tags[Index]
                        Index += 1
                    if Index == len(property_tags):
                        flag = True
                    if not flag:
                        propertyTaglist += "::"

                facility_tags = detaildata['property']['facility_tags']
                facilityTagList = ''
                flag = False
                Index = 0
                for key in facility_tags:
                    if (Index < len(facility_tags)):
                        facilityTagList += facility_tags[Index]
                        Index += 1
                    if Index == len(facility_tags):
                        flag = True
                    if not flag:
                        facilityTagList += "::"
                service_tags = detaildata['property']['service_tags']
                serviceTagList = ''
                flag = False
                Index = 0
                for key in service_tags:
                    if (Index < len(service_tags)):
                        serviceTagList += service_tags[Index]
                        Index += 1
                    if Index == len(service_tags):
                        flag = True
                    if not flag:
                        serviceTagList += "::"

                attraction_tags = detaildata['property']['attraction_tags']
                attractionTagList = ''
                flag = False
                Index = 0
                for key in attraction_tags:
                    if (Index < len(attraction_tags)):
                        attractionTagList += attraction_tags[Index]
                        Index += 1
                    if Index == len(attraction_tags):
                        flag = True
                    if not flag:
                        attractionTagList += "::"

                # 키워드 변환
                keywords = detaildata['property']['keywords']
                keywordlist = ''
                flag = False
                keywordIndex = 0
                for key in keywords:
                    if(keywordIndex < len(keywords)):
                        keywordlist += keywords[keywordIndex]
                        keywordIndex += 1
                    if keywordIndex == len(keywords):
                        flag = True
                    if not flag:
                        keywordlist += "::"
                insert_date = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                updated_date = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                with open('C:/Kong/booking/backend/newOnePick/DBConnection/onda_sql.json', 'r', encoding='utf-8') as file_json:
                    json_data = json.load(file_json)
                insert = json_data['insert']['master']
                db.execute_commit(insert, [seq, id, name, vendor_id, classlist, rating, updated_at, email,
                                           phone, website, address, detail, postal_code, latitude, longitude,
                                           checkin, checkout, property_description, reservation_description,
                                           notice_description, refund_description, refundlist, propertyTaglist,
                                           facilityTagList, serviceTagList, attractionTagList, keywordlist, insert_date,
                                           updated_date])
                break
    db.commit()
    db.close()

    return "완료시간 : " + str(dt.datetime.now())


@app.route('/delete_OndaRoomInformation', methods=['POST'])
def delete_OndaRoomInformation():
    db = pym()
    sql = 'DELETE FROM batchservice.od_accommdation_master;'

    db.excute_deleteAll(sql)
    db.commit()
    db.close()

    return "완료시간 : " + str(dt.datetime.now())


@app.route('/set_HotelStoryRoomInfomation', methods=['POST'])
def set_HotelStoryRoomInfomation():
    sbx = HotelInfo()
    data_Property = '<RequestPropertyList><Auth><AuthId>' + \
        sbx.getAuthId() + '</AuthId><AuthKey>' + sbx.getAuthKey() + \
        '</AuthKey></Auth><PropertyId></PropertyId></RequestPropertyList>'
    result = reqs.post(sbx.getUrl(), data=data_Property)

    result.encoding = 'UTF-8'
    hotelStory = xtd.parse(result.text, encoding='utf-8')

    with open('C:/Kong/booking/backend/newOnePick/DBConnection/hotelStory_sql.json', 'r', encoding='utf-8') as file_json:
        json_data = json.load(file_json)

    sql = json_data['insert']['master']
    jsn = {
        'result': ''
    }
    db = pym()

    for ids in hotelStory['ResponsePropertyList']['Propertys']['Property']:
        try:
            pid = ids['PropertyId']
            name = ids['PropertyName']
            country = ids['CountryCode']
            city = ids['CityCode']
            types = ids['PropertyType']
            rating = ids['StarRating']
            address = ids['Address']
            latitude = ids['Latitude']
            longitude = ids['Longitude']
            url = ids['HomePageUrl']
            phone = ids['Phone']
            rooms = int(ids['NumRooms'])
            checkIn = ids['CheckInTime']
            checkOut = ids['CheckOutTime']
            desc = ids['PropertyDescription']
            traffic = ids['TrafficInformation']
            instructions = ids['CheckInInstructions']

            db.execute_commit(sql, [pid, name, country, city, types, rating, address, latitude, longitude, url, phone, rooms, checkIn, checkOut,
                              desc, traffic, instructions, dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
        except pyms.err.InternalError as e:
            code, msg = e.args

            print(code, msg)

        print(hotelStory)

    db.commit()
    db.close()

    return "완료시간 : " + str(dt.datetime.now())


@app.route('/delete_HotelStoryRoomInformation', methods=['POST'])
def delete_HotelStoryRoomInformation():
    db = pym()
    sql1 = 'SET foreign_key_checks = 0;'
    sql2 = 'DELETE FROM batchservice.hs_accommodation_master;'
    sql3 = 'SET foreign_key_checks = 1;'

    db.excute_deleteAll(sql1)
    db.excute_deleteAll(sql2)
    db.excute_deleteAll(sql3)
    db.commit()
    db.close()

    return "완료시간 : " + str(dt.datetime.now())

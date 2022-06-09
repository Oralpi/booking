from newOnePick import app
import os

app.run(host='0.0.0.0', port=5000, debug=os.getenv('FLASK_DEBUG'))

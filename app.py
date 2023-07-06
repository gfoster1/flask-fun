from flask import Flask
import records

app = Flask(__name__)


if __name__ == '__main__':
    app.add_url_rule("/records", "records", records.get_Records)
    app.add_url_rule("/records/<record_id>", "records_by_id", records.get_record)
    app.run("0.0.0.0", debug=True)


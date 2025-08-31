from flask import Flask, render_template_string
from log_parser import parse_authlog, summary

TEMPLATE = """
<!doctype html>
<title>Log Monitoring Dashboard</title>
<h2>Failed Login Summary</h2>
<p>Total failed logins: <b>{{ s.total_failed_logins }}</b></p>
<table border="1" cellpadding="6">
<tr><th>#</th><th>IP</th><th>Count</th></tr>
{% for i,row in enumerate(s.top_sources, 1) %}
<tr><td>{{ i }}</td><td>{{ row.ip }}</td><td>{{ row.count }}</td></tr>
{% endfor %}
</table>
<p style="margin-top:12px;color:gray">Data source: auth.log-like file (sample included)</p>
"""

app = Flask(__name__)

@app.get("/")
def dashboard():
    df = parse_authlog()       # edit path if needed
    s = summary(df)
    return render_template_string(TEMPLATE, s=s)

if __name__ == "__main__":
    app.run(debug=True)

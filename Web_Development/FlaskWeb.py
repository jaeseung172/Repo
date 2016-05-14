from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def indexhtml():
        templateData = {
                'POST_NAME':'안녕하세요',
                'POST_NAME_SOJ':'간단한 블로그입니다, 아직 공사중입니다',
                'POST':'아직 공사중입니다<br />양해 바랍니다'
                }
        return render_template('index.html', **templateData)
	
if __name__ == "__main__":
    app.run()

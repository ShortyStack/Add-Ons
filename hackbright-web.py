from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)

    # [ (project_title, grade ), (project_title, grade )]
    grades = hackbright.get_grades_by_github(github)
    
    descriptions = hackbright.get_project_by_title(title)

    html = render_template("student_info.html", 
                            first=first,
                            last=last,
                            github=github,
                            grades=grades)
    return html

@app.route("/student-search")
def get_student_form():

    return render_template("student_search.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student"""
    first = request.form['first']
    last = request.form['last']
    github = request.form['github']
    # hackbright.session.execute("INSERT INTO hackbright VALUES('first', 'last', 'github')")
    # hackbright.session.commit()
    hackbright.make_new_student(first, last, github)

    return render_template("thank_you.html",first=first,
                            last=last,
                            github=github)
                            

@app.route("/student-add-form")
def student_add_from():

    return render_template("new_student.html")
                            # first=first,
                            # last=last,
                            # github=github)
@app.route("/project")
def project_description():
    """Returns Project: title description and max_grade"""
    
    description = hackbright.get_project_by_title(title)





if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)

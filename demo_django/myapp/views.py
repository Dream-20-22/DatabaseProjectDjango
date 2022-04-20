from django.http import HttpResponse
import mysql.connector
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def admin(request):
    if request.user.username == 'admin':
        form = '<!DOCTYPE html>' + \
           '<html>' + \
            '<style>' + \
                'th, td { background-color: #e0e0e0; }' + \
                '.center { margin-left: auto; margin-right: auto; }' + \
                'h1, h2, h3, h4 { text-align: center; }' + \
            '</style>' + \
           '<body>' + \
               '<table style="width:80%" class="center">' + \
                   '<tr>' + \
                       '<td>' + \
                           '<h1> &#9686; Administrator Panel &#9687;</h1>' + \
                           '<h2> &#9873; You can perform these functions: </h2>' + \
                        '</td>' + \
                   '</tr>' + \
                  '<tr>' + \
                       '<td>' + \
                            '<form action="f1/" method="post" style="width:80%" class="center">' + \
                            '<p> F1. List of professors sorted by: <p>' + \
                            '<INPUT TYPE=radio NAME="sort_method" VALUE="name" > Name</LABEL><BR>' + \
                            '<INPUT TYPE=radio NAME="sort_method" VALUE="dept_name"> Department</LABEL><BR>' + \
                            '<INPUT TYPE=radio NAME="sort_method" VALUE="salary"> Salary</LABEL><br><br>' + \
                            '<input type="submit" value = "submit">' + \
                            '</form>' + \
                        '</td>' + \
                   '</tr>' + \
                  '<tr>' + \
                       '<td>' + \
                            '<form action="f2/" method="post" style="width:80%" class="center">' + \
                            '<p> F2. Table of min/max/average salaries by department: <p>' + \
                                '<input type-"text" id="dept_name" name="dept_name">' + \
                                    '<label for="dept_name"> Department</label><br><br>' + \
                                '<input type="submit" value = "submit">' + \
                            '</form>' + \
                        '</td>' + \
                   '</tr>' + \
                  '<tr>' + \
                       '<td>' + \
                            '<form action="f3/" method="post" style="width:80%" class="center">' + \
                            '<p> F3. Table of professor name, department, and total number of students taught by the professor in a given semester: <p>' + \
                                '<input type-"text" id="semester_ip" name="semester_ip">' + \
                                    '<label for="semester_ip"> Semester [<b>1</b> for Fall, <b>2</b> for Spring]</label><br><br>' + \
                                '<input type="submit" value = "submit">' + \
                            '</form>' + \
                        '</td>' + \
                   '</tr>' + \
                  '<tr>' + \
                       '<td>' + \
                            '<h3><a href="/">&#9668;Home&#9658;</a></h3>' + \
                            '<h4><a href="/accounts/login/">&#10094;Log Out&#10095;</a></h4>' + \
                        '</td>' + \
                   '</tr>' + \
                '</table>' + \
           '</body>' + \
           '</html>'

        return HttpResponse(form)

    else:
        form = '<!DOCTYPE html>' + \
               '<html>' + \
               '<style>' + \
               'th, td { background-color: #e0e0e0; }' + \
               '.center { margin-left: auto; margin-right: auto; }' + \
               'h1, h2, h3, h4 { text-align: center; }' + \
               '</style>' + \
               '<body>' + \
               '<table style="width:80%" class="center">' + \
               '<tr>' + \
               '<td>' + \
               '<h1> &#9686; Please Login &#9687;</h1>' + \
               '<h2><a href="/accounts/login/">&#10094;Log in&#10095;</a></h4>' + \
               '</td>' + \
               '</tr>' + \
               '</table>' + \
               '</body>' + \
               '</html>'
        return HttpResponse(form)

@login_required(login_url='/accounts/login/')
@csrf_exempt
def f1(request):

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="DurgaPratap@1", #Change the password accordingly
        auth_plugin="mysql_native_password",
        database="university",
    )

    mycursor = mydb.cursor()

    sort = request.POST['sort_method']
    query = "select * from instructor"
    query += " order by " + sort
    query += ";"
    mycursor.execute(query)

    data = '<br>'
    data += '<h1>&#10070 Resulted List of Professors Sorted By <i>Name</i>, <i>Department</i>, or <i>Salary</i>:</h1>'
    data += '<html>'
    data +='<style>'
    data += 'th, td {border: 1px solid black;}'
    data += 'th, td { background-color: #e0e0e0; }'
    data += 'h1, h2, h3, h4 { text-align: center; }'
    data += '.center { margin-left: auto; margin-right: auto;}'
    data += '</style>'
    data += '<body style="background-color:#F4F6F6">'
    data += '<table style="width:1250px" class="center">'
    data += '<tr><th><big>Professor ID</big></th><th><big>Professor Name</big></th><th><big>Department</big></th><th><big>Salary</big></th></tr>'
    for (ID, name, dept_name, salary) in mycursor:
        r = ('<tr>' + \
             '<th>' + str(ID) + '</th>' + \
             '<th>' + str(name) + '</th>' + \
             '<th>' + str(dept_name) + '</th>' + \
             '<th>' + str(salary) + '</th>' + \
             '</t>')
        data += r
    data += '</table>'
    data += '<h3><a href="/admin/"><b>&#9668;Back&#9658;</b></a></h3>'

    mycursor.close()
    mydb.close()

    return HttpResponse(data)

@login_required(login_url='/accounts/login/')
@csrf_exempt
def f2(request):

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="DurgaPratap@1", #Change the password accordingly
        auth_plugin="mysql_native_password",
        database="university",
    )
    mycursor = mydb.cursor()
    dept = request.POST['dept_name']
    query = "select MAX(salary), MIN(salary), AVG(salary)" + \
            " from instructor " + \
            "where instructor.dept_name = \"" + dept + "\";"
    mycursor.execute(query)

    data = '<br>'
    data += '<h1>&#10070 Resulted Table of <i>Min</i>/<i>Max</i>/<i>Average</i> <i>Salaries</i> By <i>Department</i>:</h1>'
    data += '<html>'
    data +='<style>'
    data += 'th, td {border: 1px solid black;}'
    data += 'th, td { background-color: #e0e0e0; }'
    data += 'h1, h2, h3, h4 { text-align: center; }'
    data += '.center { margin-left: auto; margin-right: auto;}'
    data += '</style>'
    data += '<body style="background-color:#F4F6F6">'
    data += '<table style="width:1250px" class="center">'
    data += '<tr><th><big>Min Salary</big></th><th><big>Max Salary</big></th><th><big>Average Salary</big></th></tr>'
    for (min, max, avg) in mycursor:
        r = ('<tr>' + \
             '<th>' + str(max) + '</th>' + \
             '<th>' + str(min) + '</th>' + \
             '<th>' + str(avg) + '</th>' + \
             '</t>')
        data += r
    data += '</table>'
    data += '<h3><a href="/admin/"><b>&#9668;Back&#9658;</b></a></h3>'

    mycursor.close()
    mydb.close()

    return HttpResponse(data)

@login_required(login_url='/accounts/login/')
@csrf_exempt
def f3(request):

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="DurgaPratap@1", #Change the password accordingly
        auth_plugin="mysql_native_password",
        database="university",
    )

    mycursor = mydb.cursor()

    semester = request.POST['semester_ip']
    query = "select I.name, I.dept_name, COUNT(S.name) as count "
    query += "from instructor I, student S, teaches TC, takes TK "
    query += "where I.ID = TC.id AND TC.course_id = TK.course_id AND TK.id = S.ID "
    if semester != "":
        query += "and TK.semester = " + semester
        query += " group by I.ID"
        query += ";"
    mycursor.execute(query)

    data = '<br>'
    data += '<h1>&#10070 Resulted Table of <i>Professor Name</i>, <i>Department</i>, and <i>Number of Students</i>:</h1>'
    data += '<html>'
    data +='<style>'
    data += 'th, td {border: 1px solid black;}'
    data += 'th, td { background-color: #e0e0e0; }'
    data += 'h1, h2, h3, h4 { text-align: center; }'
    data += '.center { margin-left: auto; margin-right: auto;}'
    data += '</style>'
    data += '<body style="background-color:#F4F6F6">'
    data += '<table style="width:1250px" class="center">'
    data += '<tr><th><big>Professor Name</big></th> <th><big>Department</big></th> <th><big>Number of Students</big></th> </tr>'
    for (name, dept_name, count) in mycursor:
        r = ('<tr>' + \
             '<th>' + str(name) + '</th>' + \
             '<th>' + str(dept_name) + '</th>' + \
             '<th>' + str(count) + '</th>' + \
             '</t>')
        data += r
    data += '</table>'
    data += '<h3><a href="/admin/"><b>&#9668;Back&#9658;</b></a></h3>'

    mycursor.close()
    mydb.close()

    return HttpResponse(data)

@login_required(login_url='/accounts/login/')
def professor(request):
    if request.user.username == 'instructor':
        form = '<!DOCTYPE html>' + \
           '<html>' + \
            '<style>' + \
                'th, td { background-color: #e0e0e0; }' + \
                '.center { margin-left: auto; margin-right: auto; }' + \
                'h1, h2, h3, h4 { text-align: center; }' + \
            '</style>' + \
          '<body>' + \
               '<table style="width:80%" class="center">' + \
                   '<tr>' + \
                       '<td>' + \
                           '<h1> &#9686; Professor Panel &#9687;</h1>' + \
                           '<h2> &#9873; You can perform these functions: </h2>' + \
                        '</td>' + \
                   '</tr>' + \
                    '<tr>' + \
                       '<td>' + \
                            '<form action="f4/" method="post" style="width:80%" class="center">' + \
                            '<p> F4. List of course sections and the number of students enrolled in each section that a professor taught in a given semester: <p>' + \
                            '<input type-"text" id="course_id" name="course_id">' + \
                                '<label for="course_id"> Course ID</label><br>' + \
                                '<input type-"text" id="sec_id" name="sec_id">' + \
                                '<label for="sec_id"> Section ID</label><br><br>' + \
                                '<input type="submit" value = "submit">' + \
                            '</form>' + \
                        '</td>' + \
                   '</tr>' + \
                    '<tr>' + \
                       '<td>' + \
                            '<form action="f5/" method="post" style="width:80%" class="center">' + \
                             '<p> F5. List of students enrolled in a course section taught by a professor in a given semester: <p>' + \
                             '<input type-"text" id="instructor_name" name="instructor_name">' + \
                                '<label for="course_id"> Professor Name</label><br>' + \
                             '<input type-"text" id="semester" name="semester">' + \
                                 '<label for="semester"> Semester [<b>1</b> for Fall, <b>2</b> for Spring]</label><br>' + \
                            '<input type-"text" id="year" name="year">' + \
                                 '<label for="year"> Year</label><br><br>' + \
                            '<input type="submit" value="submit">' + \
                            '</form>' + \
                        '</td>' + \
                   '</tr>' + \
                  '<tr>' + \
                       '<td>' + \
                            '<h3><a href="/">&#9668;Home&#9658;</a></h3>' + \
                            '<h4><a href="/accounts/login/">&#10094;Log Out&#10095;</a></h4>' + \
                        '</td>' + \
                   '</tr>' + \
                '</table>' + \
           '</body>' + \
           '</html>'

        return HttpResponse(form)

    else:
        form = '<!DOCTYPE html>' + \
               '<html>' + \
               '<style>' + \
               'th, td { background-color: #e0e0e0; }' + \
               '.center { margin-left: auto; margin-right: auto; }' + \
               'h1, h2, h3, h4 { text-align: center; }' + \
               '</style>' + \
               '<body>' + \
               '<table style="width:80%" class="center">' + \
               '<tr>' + \
               '<td>' + \
               '<h1> &#9686; Please Login &#9687;</h1>' + \
               '<h2><a href="/accounts/login/">&#10094;Log in&#10095;</a></h4>' + \
               '</td>' + \
               '</tr>' + \
               '</table>' + \
               '</body>' + \
               '</html>'
        return HttpResponse(form)

@login_required(login_url='/accounts/login/')
@csrf_exempt
def f4(request):

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="DurgaPratap@1", #Change the password accordingly
        auth_plugin="mysql_native_password",
        database="university",
    )

    mycursor = mydb.cursor()

    course_id = request.POST['course_id']
    section = request.POST['sec_id']
    query = "select course_id, section, count(course_id) from" \
            " (select course.course_id as course_id, takes.id as student_id, takes.sec_id as section from " \
            "course join takes where course.course_id=takes.course_id) as courses" \

    if course_id != "":
        query += " where course_id=\"" + course_id + "\""
    if section != "":
        if course_id != "":
            query += " and section=" + section
        else:
            query += " where section=" + section
    query += " group by course_id, section;"
    mycursor.execute(query)

    data = '<br>'
    data += '<h1>&#10070 Resulted List of <i>Course Sections</i> and <i>Number of Students</i> Enrolled in <i>Each Section</i>:</h1>'
    data += '<html>'
    data +='<style>'
    data += 'th, td {border: 1px solid black;}'
    data += 'th, td { background-color: #e0e0e0; }'
    data += 'h1, h2, h3, h4 { text-align: center; }'
    data += '.center { margin-left: auto; margin-right: auto;}'
    data += '</style>'
    data += '<body style="background-color:#F4F6F6">'
    data += '<table style="width:1250px" class="center">'
    data += '<tr><th><big>Course ID</big></th><th><big>Section ID</big></th><th><big>Number of Students</big></th></tr>'
    for (course_id, sec_id, count) in mycursor:
        r = ('<tr>' +
             '<th>' + str(course_id) + '</th>' +
             '<th>' + str(sec_id) + '</th>' +
             '<th>' + str(count) + '</th>' +
             '</t>')
        data += r
    data += '</table>'
    data += '<h3><a href="/professor/"><b>&#9668;Back&#9658;</b></a></h3>'


    mycursor.close()
    mydb.close()

    return HttpResponse(data)

@login_required(login_url='/accounts/login/')
@csrf_exempt
def f5(request):

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="DurgaPratap@1", #Change the password accordingly
        auth_plugin="mysql_native_password",
        database="university",
    )

    mycursor = mydb.cursor()

    instructor = request.POST['instructor_name']
    semester = request.POST['semester']
    year = request.POST['year']
    query = "select courses.course_id course_id, courses.sec_id sec_id, courses.semester semester, courses.year year," \
            " courses.name name, teaches.id teacher_id, instructor.name instructor from teaches join instructor" \
            " join (select student.name name, course_id, sec_id, semester, year from student join takes" \
            " where student.id=takes.id) as courses where courses.course_id=teaches.course_id" \
            " and courses.semester=teaches.semester and courses.year=teaches.year and courses.sec_id=teaches.sec_id" \
            " and teaches.id=instructor.ID"

    if instructor != "":
        query += " and instructor.name=\"" + instructor + "\""
    if semester != "":
        query += " and courses.semester=" + semester
    if year != "":
        query += " and courses.year=" + year
    query += ";"
    mycursor.execute(query)

    data = '<br>'
    data += '<h1>&#10070 Resulted List of <i>Students</i> in A <i>Course Section</i> Taught By A <i>Professor</i> in A Given <i>Semester</i>:</h1>'
    data += '<html>'
    data +='<style>'
    data += 'th, td {border: 1px solid black;}'
    data += 'th, td { background-color: #e0e0e0; }'
    data += 'h1, h2, h3, h4 { text-align: center; }'
    data += '.center { margin-left: auto; margin-right: auto;}'
    data += '</style>'
    data += '<body style="background-color:#F4F6F6">'
    data += '<table style="width:1250px" class="center">'
    data += '<tr><th><big>Course ID</big></th> <th><big>Section ID</big></th> <th><big>Student Name</big></th>' + \
            '<th><big>Semester</big></th> <th><big>Year</big></th> <th><big>Professor ID</big></th> <th><big>Professor Name</big></th></tr>'
    for (course_id, sec_id, semester, year, name, teacher_id, instructor) in mycursor:
        r = ('<tr>' +
             '<th>' + str(course_id) + '</th>' +
             '<th>' + str(sec_id) + '</th>' +
             '<th>' + str(name) + '</th>' +
             '<th>' + str(semester) + '</th>' +
             '<th>' + str(year) + '</th>' +
             '<th>' + str(teacher_id) + '</th>' +
             '<th>' + str(instructor) + '</th>' +
             '</t>')
        data += r
    data += '</table>'
    data += '<h3><a href="/professor/"><b>&#9668;Back&#9658;</b></a></h3>'

    mycursor.close()
    mydb.close()

    return HttpResponse(data)

@login_required(login_url='/accounts/login/')
def student(request):
    if request.user.username == 'student':
        form = '<!DOCTYPE html>' + \
           '<html>' + \
            '<style>' + \
                'th, td { background-color: #e0e0e0; }' + \
                '.center { margin-left: auto; margin-right: auto; }' + \
                'h1, h2, h3, h4 { text-align: center; }' + \
            '</style>' + \
          '<body>' + \
               '<table style="width:80%" class="center">' + \
                   '<tr>' + \
                       '<td>' + \
                           '<h1> &#9686; Student Panel &#9687;</h1>' + \
                           '<h2> &#9873; You can perform these functions: </h2>' + \
                        '</td>' + \
                   '</tr>' + \
                    '<tr>' + \
                        '<td>' + \
                            '<form action="f6/" method="post" style="width:80%" class="center">' + \
                                 '<p> F6. List of course sections offered by department in a given semester and year: <p>' + \
                                '<input type-"text" id="department" name="department">' + \
                                     '<label for="department"> Department</label><br>' + \
                                '<input type-"text" id="semester" name="semester">' + \
                                     '<label for="semester"> Semester [<b>1</b> for Fall, <b>2</b> for Spring]</label><br>' + \
                                '<input type-"text" id="year" name="year">' + \
                                    '<label for="year"> Year</label><br><br>' + \
                                '<input type="submit" value = "Submit">' + \
                            '</form>' + \
                        '</td>' + \
                    '</tr>' + \
                  '<tr>' + \
                       '<td>' + \
                            '<h3><a href="/">&#9668;Home&#9658;</a></h3>' + \
                            '<h4><a href="/accounts/login/">&#10094;Log Out&#10095;</a></h4>' + \
                        '</td>' + \
                   '</tr>' + \
                '</table>' + \
           '</body>' + \
           '</html>'

        return HttpResponse(form)

    else:
        form = '<!DOCTYPE html>' + \
               '<html>' + \
               '<style>' + \
               'th, td { background-color: #e0e0e0; }' + \
               '.center { margin-left: auto; margin-right: auto; }' + \
               'h1, h2, h3, h4 { text-align: center; }' + \
               '</style>' + \
               '<body>' + \
               '<table style="width:80%" class="center">' + \
               '<tr>' + \
               '<td>' + \
               '<h1> &#9686; Please Login &#9687;</h1>' + \
               '<h2><a href="/accounts/login/">&#10094;Log in&#10095;</a></h4>' + \
               '</td>' + \
               '</tr>' + \
               '</table>' + \
               '</body>' + \
               '</html>'
        return HttpResponse(form)

@login_required(login_url='/accounts/login/')
@csrf_exempt
def f6(request):

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="DurgaPratap@1", #Change the password accordingly
        auth_plugin="mysql_native_password",
        database="university",
    )

    mycursor = mydb.cursor()

    department = request.POST['department']
    semester = request.POST['semester']
    year = request.POST['year']
    query = "select course.course_id, title, dept_name, sec_id, semester, year from course join teaches " + \
            "where course.course_id=teaches.course_id"
    if department != "":
        query += " and dept_name=\"" + department + "\""
    if semester != "":
        query += " and semester=\"" + semester + "\""
    if year != "":
        query += " and year=\"" + year + "\""
    query += ";"
    mycursor.execute(query)

    data = '<br>'
    data += '<h1>&#10070 Resulted List of <i>Course Sections</i> Offered By <i>Department</i> in A Given <i>Semester</i> and <i>Year</i>:</h1>'
    data += '<html>'
    data +='<style>'
    data += 'th, td {border: 1px solid black;}'
    data += 'th, td { background-color: #e0e0e0; }'
    data += 'h1, h2, h3, h4 { text-align: center; }'
    data += '.center { margin-left: auto; margin-right: auto;}'
    data += '</style>'
    data += '<body style="background-color:#F4F6F6">'
    data += '<table style="width:1250px" class="center">'
    data += '<tr><th><big>Course ID</big></th> <th><big>Course Name</big></th>' + \
            '<th><big>Department</big></th> <th><big>Section</big></th>' + \
            '<th><big>Semester</big></th> <th><big>Year</big></th></tr>'
    for (course_id, sec_id, title, dept_name, semester, year) in mycursor:
        r = ('<tr>' +
             '<th>' + str(course_id) + '</th>' +
             '<th>' + str(sec_id) + '</th>' +
             '<th>' + str(title) + '</th>' +
             '<th>' + str(dept_name) + '</th>' +
             '<th>' + str(semester) + '</th>' +
             '<th>' + str(year) + '</th>' +
             '</t>')
        data += r
    data += '</table>'
    data += '<h3><a href="/student/"><b>&#9668;Back&#9658;</b></a></h3>'

    mycursor.close()
    mydb.close()

    return HttpResponse(data)


# Student-AffairsWebSite
It is a website for student affairs. It is django project.
1) Adding a new student to the system. Student information includes id, name, date of birth, GPA, gender, level, status (”active” or “inactive”), department, email, and mobile number.
2) Updating existing student information (except department field).
3) Deleting an existing student data with a confirmation dialogue for the action before deletion occurs.
4) Searching for “active” students by name in the search for students screen and students with similar names having active status should be rendered as a table.
5) Selecting a specific student after searching to assign a department through the student’s department assignment page. The page should include the student ID, name and a dropdown list of available departments, and a submit button. This action is applicable for students if level = 3 else an error should be shown to the user with a clear understandable error message.
6) Viewing all active/inactive students on a separate page rendered in a table.
7) Changing the student status from active to inactive or vice versa from the table viewing all students.

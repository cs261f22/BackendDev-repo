**Kollen -- Sample API testing calls in HTTPie**

Note: The requests pasted here are the HTTPie commands as seen in the
"preview" section in HTTPie app, seen below:

When executing in the HTTPie app itself, the request details are
separated into the "Auth" and "Body" sections in order to pass with the
API request.

**GENERIC PAGE ACCESS TESTS:**

-   Access server default path (list path options page)

http GET localhost:8000/

-   Access server home path (list path options page)

http GET localhost:8000/home/

-   Access API default path (list API model-tables counts/entries)

http GET localhost:8000/api/

-   Access API docs page (drf-spectacular)

http GET localhost:8000/api/docs/

**API CALLS TESTS:**

-   Create student (Kollen) \-- note: this sample user is now also
    created in the db_startup command

http POST localhost:8000/api/Student/register/ \--raw \'{

\"prof\":{

\"user\":{

\"username\":\"kolleng\",

\"email\":\"gruizengak\@xavier.edu\",

\"first_name\":\"Kollen\",

\"last_name\":\"Gruizenga\",

\"password\":\"test_kg_pw\"

},

\"suffix\":\"II\"

},

\"major\":\[1, 5\],

\"minor\":\[1\],

\"schoolyear\":\"SR\"

}\'

-   Retrieve student (Kollen)

http -a \'kolleng:test_kg_pw\' GET localhost:8000/api/Student/1/

-   Create student (Aaron) \-- note: this sample user is now also
    created in the db_startup command

http POST localhost:8000/api/Student/register/ \--raw \'{

\"prof\":{

\"user\":{

\"username\":\"aaronr\",

\"email\":\"ripleya\@xavier.edu\",

\"first_name\":\"Aaron\",

\"last_name\":\"Ripley\",

\"password\":\"test_ar_pw\"

},

\"prefix\":\"Mr.\"

},

\"major\":\[1\],

\"schoolyear\":\"JR\"

}\'

-   Retrieve student (Aaron)

http -a \'aaronr:test_ar_pw\' GET localhost:8000/api/Student/2/

-   Student list students

http -a \'kolleng:test_kg_pw\' GET localhost:8000/api/Student/list/

-   Professor retrieve student (Aaron)

http -a \'mikeyg:mikey_scotch\' GET localhost:8000/api/Student/2/

-   Professor list students

http -a \'mikeyg:mikey_scotch\' GET localhost:8000/api/Student/list/

-   AA list students

http -a \'donnaw:donna_pw\' GET localhost:8000/api/Student/list/

-   Student partial-update self (Aaron)

http -a \'aaronr:test_ar_pw\' PATCH localhost:8000/api/Student/2/ \--raw
\'{

\"prof\":{

\"user\":{

\"email\":\"ripleya\@gmail.com\",

\"password\":\"new_ar_pw\"

},

\"prefix\":\"\",

\"suffix\":\"Jr.\"

},

\"major\":\[1\],

\"schoolyear\":\"JR\"

}\'

-   Student (try) partial-update student (Aaron)

http -a \'kolleng:test_kg_pw\' PATCH localhost:8000/api/Student/2/
\--raw \'{

\"prof\":{

\"user\":{

\"email\":\"ripleya\@gmail.com\",

\"password\":\"new_ar_pw\"

},

\"prefix\":\"\",

\"suffix\":\"Jr.\"

},

\"major\":\[1\],

\"schoolyear\":\"JR\"

}\'

-   Professor (try) partial-update student (Aaron)

http -a \'mikeyg:mikey_scotch\' PATCH localhost:8000/api/Student/2/
\--raw \'{

\"prof\":{

\"user\":{

\"email\":\"ripleya\@gmail.com\",

\"password\":\"new_ar_pw\"

},

\"prefix\":\"\",

\"suffix\":\"Jr.\"

},

\"major\":\[1\],

\"schoolyear\":\"JR\"

}\'

-   AA partial-update student (Aaron)

http -a \'donnaw:donna_pw\' PATCH localhost:8000/api/Student/2/ \--raw
\'{

\"prof\":{

\"user\":{

\"email\":\"ripleya\@gmail.com\",

\"password\":\"new_ar_pw\"

},

\"prefix\":\"\",

\"suffix\":\"Jr.\"

},

\"major\":\[1\],

\"schoolyear\":\"JR\"

}\'

-   Student (try) delete student (Aaron)

http -a \'kolleng:test_kg_pw\' DELETE localhost:8000/api/Student/2/
\--raw \'\'

-   Professor (try) delete student (Aaron)

http -a \'mikeyg:mikey_scotch\' DELETE localhost:8000/api/Student/2/
\--raw \'\'

-   AA delete student (Aaron)

http -a \'donnaw:donna_pw\' DELETE localhost:8000/api/Student/2/ \--raw
\'\'

-   Student delete self (Aaron)

http -a \'aaronr:test_ar_pw\' DELETE localhost:8000/api/Student/2/

-   Professor (try) create professor

http -a \'mikeyg:mikey_scotch\' POST
localhost:8000/api/Professor/register/ \--raw \'{

\"prof\":{

\"user\":{

\"username\":\"test\",

\"email\":\"test\@xavier.edu\",

\"first_name\":\"Nice\",

\"last_name\":\"Test\",

\"password\":\"test_pw\"

},

\"prefix\":\"Dr.\"

},

\"department\":4,

\"degree_desc\":\"PhD in Alpha from Penn State\"

}\'

-   AA create professor

http -a \'donnaw:donna_pw\' POST localhost:8000/api/Professor/register/
\--raw \'{

\"prof\":{

\"user\":{

\"username\":\"sommern\",

\"email\":\"sommern\@xavier.edu\",

\"first_name\":\"Nathan\",

\"last_name\":\"Sommer\",

\"password\":\"social_hr\"

},

\"prefix\":\"Dr.\"

},

\"department\":4,

\"degree_desc\":\"PhD in Computer Science from University of
Cincinnati\"

}\'

-   Student list professors

http -a \'kolleng:test_kg_pw\' GET localhost:8000/api/Professor/list/

-   Student retrieve professor

http -a \'kolleng:test_kg_pw\' GET localhost:8000/api/Professor/2/

-   Professor retrieve other professor

http -a \'mikeyg:mikey_scotch\' GET localhost:8000/api/Professor/2/

-   Professor list professors

http -a \'mikeyg:mikey_scotch\' GET localhost:8000/api/Professor/list/

-   AA retrieve professor

http -a \'donnaw:donna_pw\' GET localhost:8000/api/Professor/1/

-   AA list professors

http -a \'donnaw:donna_pw\' GET localhost:8000/api/Professor/list/

-   Professor partial-update self

http -a \'sommern:social_hr\' PATCH localhost:8000/api/Professor/2/
\--raw \'{

\"prof\":{

\"user\":{

\"username\":\"sommernNEW\",

\"email\":\"sommern\@xavier.edu\"

}

},

\"department\":5,

\"degree_desc\":\"PhD in Alpha from Penn State UNIVERSITY\"

}\'

-   AA partial-update professor

http -a \'donnaw:donna_pw\' PATCH localhost:8000/api/Professor/2/ \--raw
\'{

\"prof\":{

\"user\":{

\"username\":\"sommernTEST\",

\"email\":\"sommern\@xavier.edu\"

}

},

\"department\":5,

\"degree_desc\":\"PhD in Alpha from Penn State University\"

}\'

-   Student (try) partial-update professor

http -a \'kolleng:test_kg_pw\' PATCH localhost:8000/api/Professor/2/
\--raw \'{

\"prof\":{

\"user\":{

\"username\":\"sommern\",

\"email\":\"sommern\@xavier.edu\"

}

},

\"department\":5,

\"degree_desc\":\"PhD in Alpha from Penn State UNIVERSITY\"

}\'

-   Professor full update self

http -a \'sommernTEST:social_hr\' PUT localhost:8000/api/Professor/2/
\--raw \'{

\"prof\":{

\"user\":{

\"username\":\"sommern\",

\"email\":\"sommern\@xavier.edu\",

\"first_name\":\"Nathan\",

\"last_name\":\"Sommer\",

\"password\":\"social_hr\"

},

\"prefix\":\"Dr.\"

},

\"department\":4,

\"degree_desc\":\"BS in Computer Science from Earlham College - 2004,
PhD in Computer Science from University of Cincinnati - 2020\"

}\'

-   Student (try) delete professor

http -a \'kolleng:test_kg_pw\' DELETE localhost:8000/api/Professor/2/
\--raw \'\'

-   Professor (try) delete other professor

http -a \'mikeyg:mikey_scotch\' DELETE localhost:8000/api/Professor/2/
\--raw \'\'

-   AA delete professor

http -a \'donnaw:donna_pw\' DELETE localhost:8000/api/Professor/2/
\--raw \'\'

-   Professor delete self

http -a \'sommern:social_hr\' DELETE localhost:8000/api/Professor/2/
\--raw \'\'

-   AA create AA

http -a \'donnaw:donna_pw\' POST
localhost:8000/api/AdminAssistant/register/ \--raw \'{

\"prof\":{

\"user\":{

\"username\":\"d2test\",

\"email\":\"dw2\@xavier.edu\",

\"first_name\":\"Donna2\",

\"last_name\":\"Test\",

\"password\":\"d2test_pw\"

},

\"prefix\":\"Mrs.\"

},

\"department\":4

}\'

-   Professor (try) create AA

http -a \'mikeyg:mikey_scotch\' POST
localhost:8000/api/AdminAssistant/register/ \--raw \'{

\"prof\":{

\"user\":{

\"username\":\"AAtest\",

\"email\":\"aa\@xavier.edu\",

\"first_name\":\"newAA\",

\"last_name\":\"Test\",

\"password\":\"test_pw\"

},

\"prefix\":\"Mr.\"

},

\"department\":4

}\'

-   Professor list AAs

http -a \'sommern:social_hr\' GET
localhost:8000/api/AdminAssistant/list/

-   Student (try) list AAs

http -a \'kolleng:test_kg_pw\' GET
localhost:8000/api/AdminAssistant/list/

-   Professor retrieve AA

http -a \'mikeyg:mikey_scotch\' GET localhost:8000/api/AdminAssistant/2/

-   Student (try) retrieve AA

http -a \'kolleng:test_kg_pw\' GET localhost:8000/api/AdminAssistant/2/

-   AA retrieve other AA

http -a \'donnaw:donna_pw\' GET localhost:8000/api/AdminAssistant/2/

-   AA list AAs

http -a \'donnaw:donna_pw\' GET localhost:8000/api/AdminAssistant/list/

-   Student (try) partial-update AA

http -a \'kolleng:test_kg_pw\' PATCH
localhost:8000/api/AdminAssistant/2/ \--raw \'{

\"prof\":{

\"user\":{

\"username\":\"AAtest\",

\"email\":\"aa\@xavier.edu\",

\"first_name\":\"newAA\",

\"last_name\":\"Test\"

},

\"prefix\":\"Mr.\"

},

\"department\":4

}\'

-   Professor (try) partial-update AA

http -a \'mikeyg:mikey_scotch\' PATCH
localhost:8000/api/AdminAssistant/2/ \--raw \'{

\"prof\":{

\"user\":{

\"username\":\"AAtest\",

\"email\":\"aa\@xavier.edu\",

\"first_name\":\"newAA\",

\"last_name\":\"Test\"

},

\"prefix\":\"Mr.\"

},

\"department\":4

}\'

-   AA (try) partial-update other AA

http -a \'donnaw:donna_pw\' PATCH localhost:8000/api/AdminAssistant/2/
\--raw \'{

\"prof\":{

\"user\":{

\"username\":\"d2test-upd\",

\"email\":\"test\@xavier.edu\"

},

\"prefix\":\"Mr.\"

},

\"department\":4

}\'

-   AA partial-update self

http -a \'d2test:d2test_pw\' PATCH localhost:8000/api/AdminAssistant/2/
\--raw \'{

\"prof\":{

\"user\":{

\"username\":\"d2test-upd\",

\"email\":\"test\@xavier.edu\"

},

\"prefix\":\"Mr.\"

},

\"department\":4

}\'

-   AA full update self

http -a \'d2test-upd:d2test_pw\' PUT
localhost:8000/api/AdminAssistant/2/ \--raw \'{

\"prof\":{

\"user\":{

\"username\":\"d2test-NEW\",

\"email\":\"dw2\@xavier.edu\",

\"first_name\":\"Donna2\",

\"last_name\":\"Test\",

\"password\":\"d2_new_pw\"

},

\"prefix\":\"Mrs.\"

},

\"department\":4

}\'

-   Student (try) delete AA

http -a \'kolleng:test_kg_pw\' DELETE
localhost:8000/api/AdminAssistant/2/ \--raw \'\'

-   Professor (try) delete AA

http -a \'mikeyg:mikey_scotch\' DELETE
localhost:8000/api/AdminAssistant/2/ \--raw \'\'

-   AA (try) delete other AA

http -a \'donnaw:donna_pw\' DELETE localhost:8000/api/AdminAssistant/2/
\--raw \'\'

-   AA delete self

http -a \'d2test:d2test_pw\' DELETE localhost:8000/api/AdminAssistant/2/
\--raw \'\'

-   Student list departments

http -a \'kolleng:test_kg_pw\' GET localhost:8000/api/Departments/

-   Student retrieve department

http -a \'kolleng:test_kg_pw\' GET localhost:8000/api/Departments/3/

-   AA (try) create department

http -a \'donnaw:donna_pw\' POST localhost:8000/api/Departments/ \--raw
\'{

\"name\":\"New Department\"

}\'

-   Student list majors

http -a \'kolleng:test_kg_pw\' GET localhost:8000/api/Major/

-   AA create major

http -a \'donnaw:donna_pw\' POST localhost:8000/api/Major/ \--raw \'{

\"name\":\"BS in Wasting Time\",

\"subject\":\"Art\"

}\'

-   AA partial-update major

http -a \'donnaw:donna_pw\' PATCH localhost:8000/api/Major/9/ \--raw \'{

\"name\":\"BS in Wasting Time & Money\"

}\'

-   Student list minors

http -a \'kolleng:test_kg_pw\' GET localhost:8000/api/Minor/

-   AA create minor

http -a \'donnaw:donna_pw\' POST localhost:8000/api/Minor/ \--raw \'{

\"name\":\"Stock Analysis\",

\"subject\":\"Business\"

}\'

-   AA partial-update minor

http -a \'donnaw:donna_pw\' PATCH localhost:8000/api/Minor/7/ \--raw \'{

\"name\":\"Stock Analysis & Research\"

}\'

-   Student list HIEs

http -a \'kolleng:test_kg_pw\' GET
localhost:8000/api/HighImpactExperiences/

-   Professor create HIE

http -a \'mikeyg:mikey_scotch\' POST
localhost:8000/api/HighImpactExperiences/ \--raw \'{

\"name\":\"New CompSci HIE\",

\"RTX_name\":\"new-hie\",

\"area\":4,

\"advisor\":2,

\"Freshman_desc\":\"desc1\",

\"Sophomore_desc\":\"desc2\",

\"Junior_desc\":\"desc3\",

\"Senior_desc\":\"desc4\"

}\'

-   Student retrieve HIE

http -a \'kolleng:test_kg_pw\' GET
localhost:8000/api/HighImpactExperiences/2/

-   Professor partial-update HIE

http -a \'mikeyg:mikey_scotch\' PATCH
localhost:8000/api/HighImpactExperiences/4/ \--raw \'{

\"name\":\"Business HIE\",

\"RTX_name\":\"biz-hie\",

\"area\":6,

\"Freshman_desc\":\"description coming..\"

}\'

-   Professor delete HIE

http -a \'mikeyg:mikey_scotch\' DELETE
localhost:8000/api/HighImpactExperiences/3/

-   Student list courses

http -a \'kolleng:test_kg_pw\' GET localhost:8000/api/Courses/

-   AA create course

http -a \'donnaw:donna_pw\' POST localhost:8000/api/Courses/ \--raw \'{

\"crn\":12345,

\"title\":\"Software Engineering 2\",

\"course_num\":261,

\"subject\":4,

\"instructor\":2,

\"credit_hours\":3,

\"desc_text\":\"This is a pretty interesting course.\"

}\'

-   Student retrieve course

http -a \'kolleng:test_kg_pw\' GET localhost:8000/api/Courses/12345/

-   Professor partial-update course

http -a \'mikeyg:mikey_scotch\' PATCH localhost:8000/api/Courses/12345/
\--raw \'{

\"crn\":10300,

\"title\":\"Software Engineering 2\",

\"course_num\":261,

\"desc_text\":\"This is a pretty interesting course.\"

}\'

-   Professor delete course

http -a \'mikeyg:mikey_scotch\' DELETE localhost:8000/api/Courses/10300/

-   Student list events

http -a \'kolleng:test_kg_pw\' GET localhost:8000/api/Events/

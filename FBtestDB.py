import firebase_admin
from firebase_admin import credentials
from firebase_admin import db as firebase_db
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey2.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

#ref = db.child('Students')

data = {
    "22241A05K4":
        {
            "name": "Ekanth Sai Sundar Yellanki",
            "major": "Computer Science and Engineering",
            "Design and Analysis of Algorithms": " ",
            "Computer Organisation": " ",
            "Operating System": " ",
            "Full Stack Web Development": " ",
            "Discrete Mathematics": " ",
            "Real Time Research Project": " ",
            "Environemental Science": " ",
            "C# and VB .NET Lab": " ",
            "Full Stack Web Development Lab": " ",
            "Operating Systems Lab": " "
        },
    "22241A05D2":
        {
            "name": "Siddarth Mahesh Balijepally",
            "major": "Computer Science and Engineering",
            "Design and Analysis of Algorithms": " ",
            "Computer Organisation": " ",
            "Operating System": " ",
            "Full Stack Web Development": " ",
            "Discrete Mathematics": " ",
            "Real Time Research Project": " ",
            "Environemental Science": " ",
            "C# and VB .NET Lab": " ",
            "Full Stack Web Development Lab": " ",
            "Operating Systems Lab": " "
        },
    "22241A0506":
        {
           "name": "Sujay Anishetti",
            "major": "Computer Science and Engineering",
            "Design and Analysis of Algorithms": " ",
            "Computer Organisation": " ",
            "Operating System": " ",
            "Full Stack Web Development": " ",
            "Discrete Mathematics": " ",
            "Real Time Research Project": " ",
            "Environemental Science": " ",
            "C# and VB .NET Lab": " ",
            "Full Stack Web Development Lab": " ",
            "Operating Systems Lab": " "
        }
}

for key, value in data.items():
    ref.child(key).set(value)   
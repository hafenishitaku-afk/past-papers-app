# data.py

SUBJECTS = {
    "NSSCO": {
        "2020": [
            "Agricultural Science", "Art and Design", "Biology", "Building Studies",
            "Business Studies", "Chemistry", "Computer Science", "Design Technology",
            "Development Studies", "Economics", "English Second Language",
            "Entrepreneurship", "Fashion and Fabrics", "First Language Afrikaans",
            "First Language English", "First Language German", "First Language Khoekhoegowab",
            "First Language Oshikwanyama", "First Language Oshindonga", "First Language Otjiherero",
            "First Language Rukwangali", "First Language Rumanyo", "First Language Setswana",
            "First Language Silozi", "First Language Thimbukushu", "Foreign Language German",
            "Foreign Language Portuguese", "Geography", "History", "Home Economics",
            "Hospitality", "Integrated Performing Arts", "Mathematics", "Metalwork and Welding",
            "Motor Mechanics", "Office Practice", "Physics", "Sign Language", "Woodwork"
        ],
        "2021": [
            "Accounting", "Afrikaans Second Language", "Agricultural Science", "Art and Design",
            "Biology", "Building Studies", "Business Studies", "Chemistry", "Computer Science",
            "Design and Technology", "Development Studies", "Economics", "English Second Language",
            "English Source Papers", "Entrepreneurship", "Fashion and Fabrics", "First Language Afrikaans",
            "First Language English", "First Language German", "First Language Khoekhoegowab",
            "First Language Oshikwanyama", "First Language Oshindonga", "First Language Otjiherero",
            "First Language Rukwangali", "First Language Rumanyo", "First Language Setswana",
            "First Language Silozi", "First Language Thimbukushu", "Foreign Language German",
            "Foreign Language Portuguese", "Geography", "History", "Home Economics",
            "Hospitality", "Integrated Performing Arts", "Mathematics", "Metalwork and Welding",
            "Motor Mechanics", "Office Practice", "Physics", "Sign Language", "Woodwork"
        ],
        "2022": [
            "Accounting", "Afrikaans Second Language", "Agricultural Science", "Art and Design",
            "Biology", "Building Studies", "Business Studies", "Chemistry", "Computer Science",
            "Design and Technology", "Development Studies", "Economics", "English Second Language",
            "Entrepreneurship", "Fashion and Fabrics", "First Language Afrikaans", "First Language English",
            "First Language German", "First Language Khoekhoegowab", "First Language Oshikwanyama",
            "First Language Oshindonga", "First Language Otjiherero", "First Language Rukwangali",
            "First Language Rumanyo", "First Language Setswana", "First Language Silozi",
            "First Language Thimbukushu", "Foreign Language German", "Foreign Language Portuguese",
            "Geography", "History", "Home Economics", "Hospitality", "Integrated Performing Arts",
            "Mathematics", "Metalwork and Welding", "Motor Mechanics", "Office Practice", "Physics",
            "Sign Language", "Woodwork"
        ],
        "2023": [
            "Accounting", "Afrikaans Second Language", "Agricultural Science", "Art and Design",
            "Biology", "Building Studies", "Business Studies", "Chemistry", "Computer Science",
            "Design and Technology", "Development Studies", "Economics", "English Second Language",
            "Entrepreneurship", "Fashion and Fabrics", "First Language Afrikaans", "First Language English",
            "First Language German", "First Language Khoekhoegowab", "First Language Oshikwanyama",
            "First Language Oshindonga", "First Language Otjiherero", "First Language Rukwangali",
            "First Language Rumanyo", "First Language Setswana", "First Language Silozi",
            "First Language Thimbukushu", "Foreign Language German", "Foreign Language Portuguese",
            "Geography", "History", "Home Economics", "Hospitality", "Integrated Performing Arts",
            "Mathematics", "Metalwork and Welding", "Motor Mechanics", "Office Practice", "Physics",
            "Woodwork"
        ],
        "2024": [
            "Accounting", "Afrikaans Second Language", "Agricultural Science", "Art and Design",
            "Biology", "Building Studies", "Business Studies", "Chemistry", "Computer Science",
            "Design and Technology", "Development Studies", "Economics", "English Second Language",
            "Entrepreneurship", "Fashion and Fabrics", "First Language Afrikaans", "First Language English",
            "First Language German", "First Language Khoekhoegowab", "First Language Oshikwanyama",
            "First Language Oshindonga", "First Language Otjiherero", "First Language Rukwangali",
            "First Language Setswana", "First Language Silozi", "First Language Thimbukushu",
            "Foreign Language German", "Foreign Language Portuguese", "Geography", "History",
            "Home Economics", "Hospitality", "Integrated Performing Arts", "Mathematics",
            "Metalwork and Welding", "Motor Mechanics", "Office Practice", "Physics", "Woodwork"
        ]
    },
    "NSSCAS": {
        "2021": [
            "Accounting", "Afrikaans Second Language", "Agricultural Science", "Art and Design",
            "Biology", "Business Studies", "Chemistry", "Computer Science", "Design and Technology",
            "Economics", "English Second Language", "Entrepreneurship", "First Language Afrikaans",
            "First Language English", "First Language German", "First Language Khoekhoegowab",
            "First Language Oshikwanyama", "First Language Oshindonga", "First Language Otjiherero",
            "First Language Rukwangali", "First Language Rumanyo", "First Language Setswana",
            "First Language Silozi", "First Language Thimbukushu", "Geography", "History",
            "Mathematics", "Physics"
        ],
        "2022": [
            "Accounting", "Afrikaans Second Language", "Agricultural Science", "Art and Design",
            "Biology", "Business Studies", "Chemistry", "Computer Science", "Design and Technology",
            "Economics", "English Second Language", "Entrepreneurship", "First Language Afrikaans",
            "First Language English", "First Language German", "First Language Khoekhoegowab",
            "First Language Oshikwanyama", "First Language Oshindonga", "First Language Otjiherero",
            "First Language Rukwangali", "First Language Rumanyo", "First Language Silozi",
            "First Language Thimbukushu", "Geography", "History", "Mathematics"
        ],
        "2023": [
            "Accounting", "Afrikaans Second Language", "Agricultural Science", "Art and Design",
            "Biology", "Business Studies", "Chemistry", "Computer Science", "Design and Technology",
            "Economics", "English Second Language", "Entrepreneurship", "First Language Afrikaans",
            "First Language English", "First Language German", "First Language Khoekhoegowab",
            "First Language Oshikwanyama", "First Language Oshindonga", "First Language Otjiherero",
            "First Language Rukwangali", "First Language Rumanyo", "First Language Setswana",
            "First Language Silozi", "First Language Thimbukushu", "Foreign Language German",
            "Geography", "History", "Mathematics", "Physics"
        ],
        "2024": [
            "Accounting", "Afrikaans Second Language", "Agricultural Science", "Art and Design",
            "Biology", "Business Studies", "Chemistry", "Computer Science", "Design and Technology",
            "Economics", "English Second Language", "Entrepreneurship", "First Language Afrikaans",
            "First Language English", "First Language German", "First Language Khoekhoegowab",
            "First Language Oshikwanyama", "First Language Oshindonga", "First Language Otjiherero",
            "First Language Rukwangali", "First Language Setswana", "First Language Silozi",
            "First Language Thimbukushu", "Foreign Language German", "Geography", "History",
            "Mathematics", "Physics"
        ]
    }
}
# Goi thu vien FastAPI

from fastapi import FastAPI

# Tao doi tuong app tu class FastAPI

app = FastAPI()

# Tao decorator cho app.get(“/”) 

@app.get("/diemtoanvan")

# khi nguoi dung truy cap vao web root, goi ham sau

def get_student_scores(diemtoan: float, diemvan: float):
    return {
        "message": f"Điểm toán là {diemtoan} + {diemvan}"
    }
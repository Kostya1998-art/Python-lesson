from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://postgres:mir@localhost:5432/postgres"


def test_insert_subject():
    db = create_engine(db_connection_string)
    txt = '\"subject_id\") values (:new_name, :new_id)'
    sql = text("insert into subject(\"subject_title\","+txt)
    db.execute(sql, new_name="Russian", new_id=21)


def test_update_subject():
    db = create_engine(db_connection_string)
    txt = "update subject set subject_title = :title where subject_id = :id"
    sql = text(txt)
    db.execute(sql, {"title": "Russian", "id": 21})


def test_delete_subject():
    db = create_engine(db_connection_string)
    txt = "delete from subject where "
    sql = text(txt + "subject_title = :del_name and subject_id = :del_id")
    db.execute(sql, del_name="Russian", del_id=21)

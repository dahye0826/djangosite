import pandas as pd
import sqlite3
#csv 읽어와서
movie_file ='./../data/kmdb_get_movie_list.csv' #csv 파일

db_file = './../mysqlite.db' #데이터 베이스 파일

#전처리
def insert_movie_data():
    #movieCd 컬럼을 문자열로 인식시켜주세요
    #dtype = 데이터 타입
    movie_frame = pd.read_csv(movie_file, dtype={'movieCd': str})

    #prdYear 컬럼에 누락된 데이터는 0으로 채웁니다.
    movie_frame['prdtYear'] = movie_frame['prdtYear'].fillna(0).astype(int)
    movie_frame['repGenreNm'] = movie_frame['repGenreNm'].fillna('')
    # print(movie_frame.info())

    #sqlite3 임포트해야한다.
    #sqlite3.connect(db_file): 데이터 베이스 연결
    conn = sqlite3.connect(db_file) #접속 객체
    #cursor는 데이터베이스에서 SQL 문을 실행하고 결과를 가져오는 역할을 합니다.
    cursor= conn.cursor() #커서 객체

    for _, row in movie_frame.iterrows():
        # SQL 문이 여러 줄에 걸쳐 작성되면, """(또는 ''')을 사용해야한다.
        cursor.execute(
            """
            insert into movies(movieCd,movieNm,movieNmEn,prdtYear,openDt,typeNm,prdtStatNm,nationAlt,genreAlt,repNationNm,repGenreNm) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                row['movieCd'], row['movieNm'],row['movieNmEn'], row['prdtYear'], row['openDt'], row['typeNm'], row['prdtStatNm'], row['nationAlt'], row['genreAlt'], row['repNationNm'],
                row['repGenreNm']

            )
        )
    #end for

    conn.commit() #변경 사항 저장
    conn.close() #접속 종료
#end def insert_movie_data()

print('데이터 베이스에 추가합니다.')
insert_movie_data()
print('추가 작업이 완료 되었습니다.')
import pandas as pd
import sqlite3

coffee_file = '../data/coffeeList.csv'  # csv 파일

db_file = '../mysqlite.db'  # 데이터 베이스 파일

data_dict = {
    '브랜드': 'brand',
    '상호': 'name',
    '주소': 'address',
    '군구': 'district',
    '위도': 'latitude',
    '경도': 'longitude'
}

def insert_coffee_data():
    # movieCd 컬럼을 문자열로 인식시켜 주세요.
    coffee_frame = pd.read_csv(coffee_file)
    coffee_frame = coffee_frame.rename(columns=data_dict)

    # NaN 값을 0으로 대체
    coffee_frame[['latitude', 'longitude']] = coffee_frame[['latitude', 'longitude']].fillna(0)
    # print(coffee_frame.columns)

    conn = sqlite3.connect(db_file) # 접속 객체
    cursor = conn.cursor() # 커서 객체

    for _, row in coffee_frame.iterrows():
        cursor.execute(
            """
                insert into coffees(brand, name, address, district, latitude, longitude) values(?, ?, ?, ?, ?, ?)
            """,
            (
                row['brand'], row['name'], row['address'], row['district'], row['latitude'], row['longitude']
            )
        )
    # end for

    conn.commit()  # 변경 사항 저장
    conn.close()  # 접속 종료
# end def insert_coffee_data()

print('데이터 베이스에 추가합니다.')
insert_coffee_data()
print('추가 작업이 완료 되었습니다.')
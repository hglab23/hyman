import pyodbc
import streamlit as st

# 연결 정보를 설정합니다.
server = 'database-1.c3oa5eibtea1.us-east-2.rds.amazonaws.com'
database = 'hglab'
username = 'admin'
password = 'sasa8820'
driver = '{ODBC Driver 17 for SQL Server}'

# 연결 문자열을 만듭니다.
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

try:
    # 연결을 시작합니다.
    connection = pyodbc.connect(connection_string)
    print("MSSQL에 성공적으로 연결되었습니다.")

    # 쿼리를 실행합니다.
    cursor = connection.cursor()
    cursor.execute('SELECT wtdata FROM wt002')

    # 결과를 출력합니다.
    #for row in cursor:
    #    print(row)
    
    # st.bar_chart(view)
    
    # 결과(row)를 리스트에 저장합니다.
    row_data_list = []
    for row in cursor:
        row_data_list.append(row)  # 각 row를 리스트에 추가합니다.  
    
    # 쉼표를 제거한 새로운 리스트를 생성합니다.
    c_data_list = [int(item[0]) for item in row_data_list]
    
    st.bar_chart(c_data_list)
    # print("Row data list:", c_data_list)   
    
    
except Exception as e:
    # 연결이 실패할 경우 오류 내용을 출력합니다.
    print(f"Error: {e}")

finally:
    # 연결을 종료합니다.
    if connection:
        connection.close()
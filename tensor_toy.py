import tensorflow as tf
import numpy as np

# 판다스 엑셀파일 읽기
import pandas as pd

data = pd.read_csv('gpascore.csv')

# 비어있는 엑셀 데이터 처리
# data.isnull().sum()
# 비어있는 빈칸 데이터 제거
data = data.dropna()

# 빈 데이터에 원하는 값 삽입
data = data.fillna(100)

# 원하는 열만 출력
print(data['gpa'].min())  # .min => 최솟값 출력

y데이터 = data['admit'].values  # 합, 불 여부 리스트로
x데이터 = []


for i, rows in data.iterrows():  # iterrows : pandas데이터 프레임 데이터를 한 행씩 출력
    x데이터.append([rows['gre'], rows['gpa'], rows['rank']])


print(x데이터)


# 딥러닝 모델 만들기

model = tf.keras.models.Sequential([
    # 레이어 만들기
    # 첫번째 인자는 노드의 갯수
    # 결과물은 1개의 노드가 되야한다.
    # 마지막 레이어는 1개 / 결과를 여러개를 뽑고 싶다면 여러개여야 겠죠?
    # 두번째 인자는 활성함수
    # sigmoid 는 0~1 사이의 확률을 출력하고 싶을때 사용
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])

# 컴파일까지 해줘야 모델이 완성됨
# optimizer = 가중치에 빼는 값을 조절해줌
# loss = 손실함수 / binary_crossentropy => 0 인지 1인지 확률을 예측할때 유용
model.compile(optimizer='adam', loss='binary_crossentropy',
              metrics=['accuracy'])

# 학습시키기

# epochs 학습 반복수
# 파이썬 리스트로 데이터를 넘겨주면 에러가 난다!! numpy 사용하자
model.fit(np.array(x데이터), np.array(y데이터), epochs=1000)

# 예측

# 성적이 gre가 700 학점 3.7 Rank 4 합격확률은?
# 성적이 gre가 400 학점 2.2 Rank 1 합격확률은?
# 위 모델로 예측

예측값 = model.predict([[700, 3.70, 3],[400, 2.2, 1]])

print(예측값)
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# 키 = [170, 180, 175, 160]
# 신발 = [260, 270, 265, 255]

# y = ax + b 
# y는 신발 x는 키
# 키를 대입하면  ??? = a 170 + b -> a와 b를 구할 수 있어야함

# 신발 = a*키 + b

키 = 170
신발 = 260

# 신발 = 키 * a + b

# 가중치 만들기
a = tf.Variable(0.1)
b = tf.Variable(0.2)


# 손실함수

def 손실함수():
    예측값 = 키 * a + b
    return tf.square(260 - 예측값)

# return 손실값 > 실제값 - 예측값 (오차)
# tf.square 제곱 해서 계산됨

# 경사하강법
opt = tf.keras.optimizers.Adam(learning_rate=0.1) 
# gradient를 알아어 스마트하게 바꿔줌

# 경사하강 실행 (손실함수, var_list = []) 
# a, b 업데이트


for i in range(300):
    opt.minimize(손실함수, var_list = [a,b])
    print(a.numpy(), b.numpy())
    

# a,b 값은 1.5198832 1.6198832

# 예측한 신발사이즈 = 키*1.52 + 1.62
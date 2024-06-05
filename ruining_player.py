#%% md
# # Разорение игрока
#%%
import random
#%% md
# ## Исходные данные
# Вариант 18
#%%
p = 0.44 # Вероятность выйгарть у 1 игрока 

# Количество денег 
y = 153 # Баланс 1 игрока 
x = 76 # Баланс 2 игрока 

N = 1000 # количество игр
N_game = 1000 # количество раундов
#%% md
# Получение случайного значения от 0 до 1 с точность до 0.01
#%%
def random_num():
        return round(random.uniform(0, 1), 2)
#%%
def sparing():
    
    vin_1 = 0
    vin_2 = 0
    none_ = 0
    over_game = []
    
    for _ in range(N_game):
        balans = 0 
        count = 0
        for _ in range(N):
            
            random_nums = random_num()
            
            if random_nums <= p:
                balans += 1
            else:
                balans -= 1
                
            if balans >= y:
                vin_1 += 1
                break
                
            if balans <= -x:
                vin_2 += 1
                break

            count += 1       

        over_game.append(count)
        # Если число игр закончилось, то проверяем кто выйграет 
        if count == N:
            if balans < 0:
                vin_1 += 1
            elif balans > 0:
                vin_2 += 1
            else:
                none_ += 1
                
    sp_game = int(sum(over_game)/len(over_game))
    
    winner = 1 if vin_1 > vin_2 else 2
    
    print(f"Победит игрок: {winner} \n")
    
    print(f"Общеe число игр: {N_game} \n")
    
    print(f"Количестов побед у 1 игрока: {vin_1}\n"
          f"Количестов побед у 2 игрока: {vin_2}\n")
    print(f"ср длительность игры: {sp_game}")
    print(
            f"\nПроцент побед у 1 игрока  = {vin_1/N_game}"
            f"\nПроцент побед у 2 игрока = {vin_2/N_game}"
            f"\nПроцент ничьих = {none_/N_game}"
            f"\nпроверка = {(vin_1/N_game)+(vin_2/N_game)+(none_/N_game)} ")
#%%
sparing()
#%%

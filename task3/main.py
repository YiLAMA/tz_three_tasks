from typing import List, Dict, Any
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/")
def root():
    return f"message: Welcome to FastAPI"


@app.post("/task3/")
def appearance(intervals: Dict[str, List[int]]) -> int:
    """Функция вычисляет время общего присутствия ученика и учителя на уроке (в секундах)"""
    sum_sec = 0
    len_pupil = len(intervals['pupil'])
    len_tutor = len(intervals['tutor'])
    for kp in range(0, len_pupil, 2):
        # Если ученик зашел и вышел ДО урока, то пропускаем его "время"
        if intervals['pupil'][kp + 1] <= intervals['lesson'][0]:
            continue
        # Если ученик зашел и вышел ПОСЛЕ урока, то пропускаем его "время"
        if intervals['pupil'][kp] >= intervals['lesson'][1]:
            continue

        # Если ученик был до урока и остался (присутствовал) на уроке
        if intervals['pupil'][kp] <= intervals['lesson'][0] <= intervals['pupil'][kp + 1]:
            intervals['pupil'][kp] = intervals['lesson'][0]
        # Если ученик был во время урока и остался после окончания
        if intervals['pupil'][kp] <= intervals['lesson'][1] <= intervals['pupil'][kp + 1]:
            intervals['pupil'][kp + 1] = intervals['lesson'][1]

        for kt in range(0, len_tutor, 2):
            # Если учитель зашел и вышел ДО урока, то пропускаем его "время"
            if intervals['tutor'][kt + 1] <= intervals['lesson'][0]:
                continue
            # Если учитель зашел и вышел ПОСЛЕ урока, то пропускаем его "время"
            if intervals['tutor'][kt] >= intervals['lesson'][1]:
                continue

            # Если учитель был до урока и остался (присутствовал) на уроке
            if intervals['tutor'][kt] <= intervals['lesson'][0] <= intervals['tutor'][kt + 1]:
                intervals['tutor'][kt] = intervals['lesson'][0]
            # Если учитель был во время урока и остался после окончания
            if intervals['tutor'][kt] <= intervals['lesson'][1] <= intervals['tutor'][kt + 1]:
                intervals['tutor'][kt + 1] = intervals['lesson'][1]

            # Если ученик был во время урока (присутствовал)
            if intervals['lesson'][0] <= intervals['pupil'][kp] <= intervals['lesson'][1]:
                pupil_start = intervals['pupil'][kp]
                # Если учитель был во время урока (присутствовал)
                if intervals['lesson'][0] <= intervals['tutor'][kt] <= intervals['lesson'][1]:
                    tutor_start = intervals['tutor'][kt]
                    # Если ученик присутствовал до учителя и они встретились
                    if tutor_start <= pupil_start <= intervals['tutor'][kt + 1]:
                        appear_start = pupil_start
                    # Если ученик присутствовал после учителя и они встретились
                    elif pupil_start <= tutor_start <= intervals['pupil'][kp + 1]:
                        appear_start = tutor_start
                    # Если не встретились, то следующее "время"
                    else:
                        continue

                    # Если ученик отключился до учителя
                    if tutor_start <= intervals['pupil'][kp + 1] <= intervals['tutor'][kt + 1]:
                        appear_end = intervals['pupil'][kp + 1]
                    # Если ученик отключился после учителя
                    elif pupil_start <= intervals['tutor'][kt + 1] <= intervals['pupil'][kp + 1]:
                        appear_end = intervals['tutor'][kt + 1]
                    # Если зашли и вышли (присутствовали) НЕ в одну и ту же секунду
                    if appear_end != appear_start:
                        # То считаем общее время присутствия ученика и учителя
                        sum_sec += appear_end - appear_start

    return {"Время общего присутствия ученика и учителя на уроке (в секундах):": sum_sec}
    # return sum_sec


"""
Пример, когда ученик и учитель были онлайн только во время урока
{
    "lesson": [1594663200, 1594666800],
    "pupil": [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
    "tutor": [1594663290, 1594663430, 1594663443, 1594666473]
}

Пример, когда ученик и учитель были онлайн ДО и во время урока
{
    "lesson": [1594663200, 1594666800],
    "pupil": [1594663200, 1594663250, 1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
    "tutor": [1594663170, 1594663260, 1594663290, 1594663430, 1594663443, 1594666473]
}
Пример, когда ученик и учитель были онлайн ДО, во время урока и оставались ПОСЛЕ
{
    "lesson": [1594663200, 1594666800],
    "pupil": [1594663200, 1594663250, 1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472, 1594666770, 1594666870],
    "tutor": [1594663170, 1594663260, 1594663290, 1594663430, 1594663443, 1594666473, 1594666740, 1594666840]
}
"""

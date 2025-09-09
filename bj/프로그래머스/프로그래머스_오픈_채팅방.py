from collections import defaultdict
# 문자열 배열 파싱 Enter, Leave, Change
# 딕셔너리 생성 {아이디,[닉네임,상태코드]}
#
# Enter면 들어왔습니다 Leave 면 나갔습니다

def solution(record):

    sequence = []
    answer = []
    user_record = defaultdict(lambda: [[], []]) # uid1234: [["muzi"],["enter"]]
    for user_status in record:   #[[Enter],[Uid1234],[Muzi]]
        user_status = user_status.split(" ")
        if len(user_status) == 3:

            user_record[user_status[1]][0] = user_status[2]
            sequence.append(user_status[1])
            user_record[user_status[1]][1].append(user_status[0])
        elif len(user_status) == 2:
            user_record[user_status[1]][1].append(user_status[0])
            sequence.append(user_status[1])

    for user in sequence:
        s = ""
        item = user_record[user]
        nick_name = item[0]

        if item[1][0] == "Enter":
                s = (f"{nick_name}님이 들어왔습니다.")
                answer.append(s)
                user_record[user][1].pop(0)
        elif item[1][0] == "Leave":
            s = (f"{nick_name}님이 나갔습니다.")
            answer.append(s)
            user_record[user][1].pop(0)
        elif item[1][0] == "Change":
        # s = (f"{nick_name}님이 나갔습니다.")
        # answer.append(s)
            user_record[user][1].pop(0)












    # temp = user_status.split(" ")
    # if len(temp) == 3:
    #     user_record_status = user_record[temp[1]][1]
    #     user_record[temp[1]] = [temp[2],[user_record_status,temp[0]]]
    # if len(temp) == 2:
    #     user_record_status = user_record[temp[1]][1]
    #     user_record[temp[1]] = [user_record_status,temp[0]]
    #         if temp[0] != "Leave":
    #             user_record[temp[1]] = [temp[2],temp[0]]
    #         elif temp[0] == "Leave":
    #             user_nickname = user_record[temp[1]][0]
    #             user_record[temp[1]] = [user_nickname,temp[0]]

    #     for _ in user_record:
    #         item = _.items()
    #         if item[1][1]
    #         result = f"{item[1][0]}님이 들어왔습니다"

    print(answer)
    return answer



# 딕셔너리에 이중 리스트에 추가하는 법을 몰라서 막힘
# 문제에서 결국 사용자의 입장과 퇴장 상태를 저장해야 하는데 이 부분을 놓침
#
para = ["Enter uid1 A", "Change uid1 B", "Leave uid1"]


solution(para)




# from collections import defaultdict
#
# def solution(record):
#
#     sequence = []
#     answer = []
#     user_record = defaultdict(lambda: [[], []])
#     for user_status in record:
#         user_status = user_status.split(" ")
#         if len(user_status) == 3:
#
#             user_record[user_status[1]][0] = user_status[2]
#             sequence.append(user_status[1])
#             user_record[user_status[1]][1].append(user_status[0])
#         elif len(user_status) == 2:
#             user_record[user_status[1]][1].append(user_status[0])
#             sequence.append(user_status[1])
#
#     for user in sequence:
#         s = ""
#         item = user_record[user]
#         nick_name = item[0]
#
#         if item[1][0] == "Enter":
#                 s = (f"{nick_name}님이 들어왔습니다.")
#                 answer.append(s)
#                 user_record[user][1].pop(0)
#         elif item[1][0] == "Leave":
#             s = (f"{nick_name}님이 나갔습니다.")
#             answer.append(s)
#             user_record[user][1].pop(0)
#         elif item[1][0] == "Change":
#
#             user_record[user][1].pop(0)
#
#
#     return answer
# 최종 풀이 코드, change 로직을 안 만들어서 문제가 됐음 꼭 문제에서 말하는 조건은 다 만들언 놓자!!!!!
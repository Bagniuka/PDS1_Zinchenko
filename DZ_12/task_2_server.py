import socket
import asyncio

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', 55555))
    s.listen()
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024).decode()
        num_lst = []
        for i in data:
            i = int(i)
            num_lst.append(i)


        async def addition(nums):
            add_nums = nums[0] + nums[1]
            return add_nums


        async def subtraction(nums):
            sub_nums = nums[0] - nums[1]
            return sub_nums


        async def multiplication(nums):
            mul_nums = nums[0] * nums[1]
            return mul_nums


        oploop = asyncio.get_event_loop()
        tasks = [
            oploop.create_task(addition(num_lst)),
            oploop.create_task(subtraction(num_lst)),
            oploop.create_task(multiplication(num_lst))
        ]
        oploop.run_until_complete(asyncio.wait(tasks))

        message = f'Addition values is: {tasks[0].result()};\n' \
                  f'Subtraction values is {tasks[1].result()};\n' \
                  f'Multiplication values is {tasks[2].result()}.'

        conn.sendall(message.encode())

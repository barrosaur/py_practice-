from datetime import datetime as dt

# My own exception
class InvalidModeError(Exception):
  pass

def read_logs(**kwargs):
  mode = kwargs.get("mode")

  if mode == "r":
    with open("token_logs.txt", "r") as file:
      token_logs = file.readlines()

    for log in token_logs:
      print(log)
  else:
    raise InvalidModeError(f"Mode invalid: {mode}")
  
def write_to_logs(**kwargs):
  token = kwargs.get("token")

  with open("token_logs.txt", "a") as file:
    line = str(dt.now()) + "\t" + token + "\n"
    file.writelines(line)
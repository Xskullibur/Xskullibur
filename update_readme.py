from datetime import datetime
import pytz
import re

def get_current_time():
    sg_tz = pytz.timezone('Asia/Singapore')
    current_time = datetime.now(sg_tz)
    return current_time.strftime("%a, %d %b %Y at %H:%M:%S +08")

def update_readme():
    with open('README.md', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Update the timestamp in the login line
    new_content = re.sub(
        r'Last login: .*? from',
        f'Last login: {get_current_time()} from',
        content
    )
    
    # Write the updated content
    with open('README.md', 'r+', encoding='utf-8') as file:
        file.write(new_content)

if __name__ == "__main__":
    update_readme()
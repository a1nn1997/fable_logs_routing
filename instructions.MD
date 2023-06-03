# Steps for installation:
    1. run setup.sh for mac and ubuntu user or run commands present in setup.sh file

    2. username and password for admin panel is user

    3. admin url : http://127.0.0.1:8050/admin/

    4. log api curl : 
            curl --location --request POST 'http://127.0.0.1:8050/log/' \
            --header 'Content-Type: application/json' \
            --data-raw '{
            "id": 1234,
            "unix_ts": 1684129671,
            "user_id": 123456,
            "event_name": "login"
            }'
    
    5. sets of commands for windows users:
        docker-compose down - v
        docker-compose up --build -d
        docker-compose -f docker-compose-test.yml run tests

    6. sets of commands for ubuntu, mac users
        sh setup.sh


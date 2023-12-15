## Technical task:
```
task 1:

    Implement own hashmap class (put, get methods are required).
    write tests for this class.
    add notes with argumentation for choosen implementation.

task 2:
    Write small service class with methods
    get(user_id) → UserDTO
    add(user: UserDTO)

    signatures can be changed if you think it's needed for better implementation

    UserDTO - pydantic model
    users are stored in db.
    assume you have method get_async_session, which returns AsyncSession sqlalchemy object to interact with db

    write tests for that class.
    
    add notes with argumentation for choosen implementation.

```

## Installation:

1. Clone from git:
    ```shell
    git clone https://github.com/Tezlaa/test_for_prostopay.git
    ```

2. You can start bash script or manual setuping.

 

#### Start `starttests.sh`
#### Manual setup: 
1. Create virtual environment:
    - *Windows*:
    ```shell
        python -m venv venv
    ```
    - *Unix*:
    ```shell
        python3.11 -m venv venv
    ```
2.  Activate virtual environment: 
    - *Windows*:
    ```shell
        .\venv\Scripts\activate
    ```
    - *Unix*:
    ```shell
        source .\venv\bin\activate
    ```
3. Install requirements for tasks:
    ```shell
    pip install -r requirements.txt
    ```
4. Test **task-1**:
    ```shell
    cd task1/
    pytest
    ```
    ```shell
    cd ..
    ```
5. Test **task-2**:
    ```shell
    cd task2/
    ```
    ```shell
    mv .env-copy .env
    ```
    ```shell
    pytest
    ```
    ```shell
    cd ..
    ```
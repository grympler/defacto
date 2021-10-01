# Goal

Build a toy coding game plateform.

## Mandatory

* Get a list of all challenges.
* For every challenge get detailled instructions on what to send, input and expected output.
* For every challenge be able to post a solution and get a feedback on success or not.

## Follow up

* Detailled log failure for the user
* Improved client
* Timeout
* Solve challenges
* Add our own challenge
* Testsuit
* Security of remote code execution
* ...

## What's provided

* A client `client.py` is provided to POST a request on `http://127.0.0.1/challenge/1`. See `client.py --help for more informations`. Feel free to adapt the client code.
* A data directory with 2 challenges. In each subdirectory (one per challenge) two files are provided. One README with detailed instruction on the challenge and one test.json file with a list of tests.

test.json:
```
[
    [input, expected_output] # input is a list (passed as *args to the test functions)
]
```

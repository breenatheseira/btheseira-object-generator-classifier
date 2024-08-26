## A challenge to create and classify objects based on their type.

This program uses Python 3.12.5 and its core libraries.

The command line instructions to complete each challenge is as below:

### Challenge A:

A new file will be generateed, stored in the `results` folder, named `random-objects.txt`.

It contains the results from `python3 object_generator.py`, which is used to feed the command for Challenge B.

```
git clone https://github.com/breenatheseira/btheseira-object-generator-classifier.git
cd btheseira-object-generator-classifier
python3 object_generator.py
```

---

### Challenge B:

The below command prints the results in the console (it may be really fast).

If an error occurs, please ensure that the `python3 object_generator.py` command has been run.

```
python3 file_reader.py
```

---

### Challenge C:

Note: depending on your Docker set-up `sudo` may need to be prefixed to the following commands, ie.
`sudo docker compose build`.

While the container is running, the output of Challenge B will not be printed on the console.

A new file will be generated, stored in the `results` folder, named `classified.txt`.
```
docker compose build
docker compose up
```

# Group 75 xss demo

# setup
create a virtual environment and install flask or use an existing environment that has flask

# Run Back end
Run the following in separate terminal instances

```
python backend.py
```

```
python fake_backend.py
```

# Front end
open index.html with your browser

To see an xss injection submit the following

```
</a></li><li><a href="http://localhost:8001/listing/1">fake listing
```

from yoyo import step
steps = [
   step(
       'CREATE TABLE customers (id INT AUTO_INCREMENT, name VARCHAR(20), email VARCHAR (250) ,PRIMARY KEY (id) )',
       "DROP TABLE customers"
   )
]
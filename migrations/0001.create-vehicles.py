from yoyo import step
steps = [
   step(
       "CREATE TABLE vehicles (id INT AUTO_INCREMENT, type TINYINT(20),available TINYINT(20), PRIMARY KEY (id))",
       "DROP TABLE vehicles"
   )
]
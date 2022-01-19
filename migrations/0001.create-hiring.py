from yoyo import step

steps = [
    step(
        "CREATE TABLE hiring(id INT AUTO_INCREMENT, customer_id INT NOT NULL,vehicle_id int not NULL ,start_date VARCHAR(250), return_date VARCHAR(250), price double(2,1), PRIMARY KEY (id) )",
        "DROP TABLE hiring"
    ), step(
        "ALTER TABLE hiring ADD FOREIGN KEY(customer_id) REFERENCES customers(id)",
        'ALTER TABLE hiring ADD FOREIGN KEY(vehicle_id) REFERENCES vehicles(id)'

    )
]

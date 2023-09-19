from SQLOperations import MSSQLDatabase

if __name__=="__main__":
    """
    burada with keyword u nesnelerin otomatik olarak başlamasını ve işlem sonunda temizlenmesini sağlar
    bu da bağlantıların düzgün bir şekilde açılıp kapatılması için kullandım
    """
    with MSSQLDatabase(".","deneme") as db:
        db.create_table("_table","name VARCHAR(100) ,surname VARCHAR(100),AGE INT")
        db.insert_data("_table","('yavuz','aydin',25)")
        print("Veriler : ")
        db.show_data("_table")
        db.delete_data("_table","name = 'yavuz'")
        print("Veriler (sildikten sonra) : ")
        db.show_data("_table")
        db.drop_table("_table")






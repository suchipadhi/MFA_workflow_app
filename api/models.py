from sqlalchemy import Table, Column, Integer, String, DateTime, MetaData, Sequence

metadata = MetaData()

users = Table(
    "py_users", metadata,
    Column('id', Integer, Sequence("user_id_seq"), primary_key=True),
    Column('email', String(100)),
    Column('password', String(100)),

)
opts = Table(
    "py_emails", metadata,
    Column("id", Integer, Sequence('otp_id_se‚q'), primary_key=True),
    Column("recipent_id", String(100)),
    Column("session_id", String(100)),
    Column("otp_code", String(100)),
    Column("created_on", String(100))


)


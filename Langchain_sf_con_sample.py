
from langchain.document_loaders import SnowflakeLoader

QUERY = "select * from analytics.raw.customer limit 10"
snowflake_loader = SnowflakeLoader(
    query=QUERY,
    user="WILL2308",
    password="Wilk00023*",
    account="https://mafkuyr-lt58083.snowflakecomputing.com",
    warehouse="COMPUTE_WH",
    role="ACCOUNTADMIN",
    database="analytics",
    schema="raw",
)
snowflake_documents = snowflake_loader.load()
i=1
for document in snowflake_documents:
    print("row number = {} =======================".format(i))
    print(document.page_content)
    i=i+1

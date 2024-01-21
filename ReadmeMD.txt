Adoption_DB: Talk to a Database

This is an end to end LLM project based on Google Palm and Langchain. I have builded a system that can talk to MySQL database. User asks questions in a natural language and the system generates answers by converting those questions to an SQL query and then executing that query on MySQL database. Adoption_DB is a Database which contains the Tree Details where I maintain their Quantity, Tree name and many attributes in various region(Ooty,Yercaud) data in MySQL database. A store manager will may ask questions such as,

How many Pine Trees are avilable in Oooty Farm?
How much Quantity of Cedar trees will be availble in Both OOty and Yercaud and their estimated Production cost? The system is intelligent enough to generate accurate queries for given question and execute them on MySQL database


Project Highlights
I builded an LLM based question and answer system that will use following,
Google Palm LLM
Streamlit for UI
Langchain framework
Chromadb as a vector store
Few shot learning
In the UI, store manager will ask questions in a natural language and it will produce the answers.
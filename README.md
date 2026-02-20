## Medal_ranking (Python & SQL)
A Python script that determines the Olympic 2026 medal color based on the athelte's score. Also, implement ** persistent data storage** using SQL database.

Architected a data-driven application by independently learning RDBMS principles. Selected SQLite for local storage efficiency and resolved data persistence issues by ensuring records are reliably stored across sessions. Implemented parameterized queries to mitigate SQL injection risks, demonstrating a proactive and security-first approach to software development.

## Overview
- 158 or more: Gold Medal and word record
- 152 or more: Gold Medal
- 145 to 149: Silver Medal
- 142 to 144: Bronze Medal
- Below 142: No Medal

## Key Features
**Persistent data storage**: Integrated **SQLite** to ensure athlete records are saved and survive program restarts.
**Robust Error Handling**: Implemented 'try-except-finally' blovks to manage invalid user inputs and ensure database are closed.

## Technical highlights
**Relational Database Management**: Created and managed SQL schems using Python's 'sqlite3' library, including primary keys.
**Security & Data integrity**: Utilized parameterized SQL queries (using '?" placeholders) to ensure secure data insertion.

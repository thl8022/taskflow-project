from src.database import get_connection


def get_all_tasks():
    conn = get_connection()

    tasks = conn.execute(
        """
        SELECT *
        FROM tasks
        ORDER BY id DESC
        """
    ).fetchall()

    conn.close()

    return tasks


def get_tasks_by_priority(priority):

    conn = get_connection()

    tasks = conn.execute(
        """
        SELECT *
        FROM tasks
        WHERE priority = ?
        ORDER BY id DESC
        """,
        (priority,)
    ).fetchall()

    conn.close()

    return tasks


def get_task_by_id(task_id):

    conn = get_connection()

    task = conn.execute(
        """
        SELECT *
        FROM tasks
        WHERE id = ?
        """,
        (task_id,)
    ).fetchone()

    conn.close()

    return task


def create_task(title, description, priority, status):

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO tasks
        (title, description, priority, status)
        VALUES (?, ?, ?, ?)
        """,
        (title, description, priority, status)
    )

    conn.commit()
    conn.close()


def update_task(task_id, title, description, priority, status):

    conn = get_connection()

    conn.execute(
        """
        UPDATE tasks
        SET
            title=?,
            description=?,
            priority=?,
            status=?
        WHERE id=?
        """,
        (
            title,
            description,
            priority,
            status,
            task_id
        )
    )

    conn.commit()
    conn.close()


def delete_task(task_id):

    conn = get_connection()

    conn.execute(
        """
        DELETE FROM tasks
        WHERE id=?
        """,
        (task_id,)
    )

    conn.commit()
    conn.close()


def get_dashboard_stats():
    conn = get_connection()

    total = conn.execute(
        "SELECT COUNT(*) FROM tasks"
    ).fetchone()[0]

    pending = conn.execute(
        "SELECT COUNT(*) FROM tasks WHERE status='Pendente'"
    ).fetchone()[0]

    progress = conn.execute(
        "SELECT COUNT(*) FROM tasks WHERE status='Em andamento'"
    ).fetchone()[0]

    completed = conn.execute(
        "SELECT COUNT(*) FROM tasks WHERE status='Concluído'"
    ).fetchone()[0]

    conn.close()

    return {
        "total": total,
        "pending": pending,
        "progress": progress,
        "completed": completed
    }

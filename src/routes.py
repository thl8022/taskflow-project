from flask import render_template, request, redirect, url_for

from src.services import (
    get_all_tasks,
    get_tasks_by_priority,
    get_task_by_id,
    create_task,
    update_task,
    delete_task,
    get_dashboard_stats
)


def register_routes(app):

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/dashboard")
    def dashboard():

        priority = request.args.get("priority")

        if priority:
            tasks = get_tasks_by_priority(priority)
        else:
            tasks = get_all_tasks()

        stats = get_dashboard_stats()

        return render_template(
            "dashboard.html",
            tasks=tasks,
            stats=stats,
            selected_priority=priority
        )

    @app.route("/new", methods=["GET", "POST"])
    def new_task():

        if request.method == "POST":

            create_task(
                request.form["title"],
                request.form["description"],
                request.form["priority"],
                request.form["status"]
            )

            return redirect(url_for("dashboard"))

        return render_template("task_form.html")

    @app.route("/edit/<int:task_id>", methods=["GET", "POST"])
    def edit_task(task_id):

        task = get_task_by_id(task_id)

        if request.method == "POST":

            update_task(
                task_id,
                request.form["title"],
                request.form["description"],
                request.form["priority"],
                request.form["status"]
            )

            return redirect(url_for("dashboard"))

        return render_template(
            "task_form.html",
            task=task
        )

    @app.route("/delete/<int:task_id>")
    def remove_task(task_id):

        delete_task(task_id)

        return redirect(url_for("dashboard"))

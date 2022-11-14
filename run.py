from app import initialize_app

app = initialize_app()
if __name__ == '__main__':
    app.run(debug=False)  # Do not use debug=True in production

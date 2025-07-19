{
  "configurations": [
    {
      "name": "AgroAnalyst (Secure Mode)",
      "type": "python",
      "request": "launch",
      "program": "${workspaceRoot}\\main.py",
      "args": ["--security-level=high"],
      "env": {
        "PYTHONPATH": "${workspaceRoot}",
        "APP_ENV": "development"
      },
      "python": {
        "command": "venv\\Scripts\\python.exe"
      }
    },
    {
      "name": "Run with AI Debug",
      "type": "python",
      "request": "launch",
      "program": "${workspaceRoot}\\main.py",
      "args": ["--debug-ai"],
      "justMyCode": false
    }
  ]
}
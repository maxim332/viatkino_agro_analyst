viatkino_agro_analyst/
├── main.py
├── config/
│   ├── __init__.py
│   ├── settings.py
│   └── security_config.py
├── core/
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   └── utils.py
├── services/
│   ├── __init__.py
│   ├── climate_service.py
│   ├── prediction_service.py
│   ├── security_service.py
│   └── analytics_service.py
├── ai/
│   ├── __init__.py
│   ├── anomaly_detection.py
│   ├── security_ai.py
│   ├── decision_system.py
│   └── adaptive_learning.py
├── security/
│   ├── __init__.py
│   ├── active_defense.py
│   ├── ai_antivirus.py
│   ├── encryption.py
│   └── ai_security_guard.py
├── data_processing/
│   ├── __init__.py
│   ├── data_fetchers.py
│   ├── data_cleaners.py
│   └── data_transformers.py
├── ui/
│   ├── __init__.py
│   ├── main_window.py
│   ├── tabs/
│   │   ├── __init__.py
│   │   ├── dashboard_tab.py
│   │   ├── data_entry_tab.py
│   │   ├── analytics_tab.py
│   │   ├── prediction_tab.py
│   │   └── admin_tab.py
│   ├── widgets/
│   │   ├── __init__.py
│   │   ├── climate_widget.py
│   │   ├── econ_widget.py
│   │   └── map_widget.py
│   ├── dialogs/
│   │   ├── __init__.py
│   │   ├── login_dialog.py
│   │   ├── location_dialog.py
│   │   └── settings_dialog.py
│   └── voice_interface.py
├── resources/
│   ├── icons/
│   │   ├── app_icon.png
│   │   ├── climate_icon.png
│   │   └── analytics_icon.png
│   ├── translations/
│   │   ├── en_US/
│   │   │   ├── LC_MESSAGES/
│   │   │   │   └── messages.mo
│   │   │   └── ui_strings.json
│   │   └── ru_RU/
│   │       ├── LC_MESSAGES/
│   │       │   └── messages.mo
│   │       └── ui_strings.json
│   └── geo_data/
│       ├── agro_zones.geojson
│       └── crop_suitability.json
├── models/
│   ├── crop_yield/
│   │   ├── wheat_rf_model.joblib
│   │   └── sunflower_model.pkl
│   ├── anomaly_detection/
│   │   └── anomaly_model.joblib
│   └── security/
│       └── threat_model.pt
├── data/
│   ├── db/
│   │   └── viatkino_agro.db
│   ├── cache/
│   │   └── nasa_climate_cache
│   └── exports/
├── logs/
│   ├── application.log
│   ├── security.log
│   └── ai_performance.log
├── tests/
│   ├── unit/
│   │   ├── test_database.py
│   │   └── test_analytics.py
│   └── integration/
│       └── test_full_flow.py
├── scripts/
│   ├── db_init.py
│   ├── model_trainer.py
│   └── data_importer.py
├── docs/
│   ├── architecture.md
│   ├── api_docs/
│   └── user_manual/
├── .env
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.mdimport sys

from PyQt6.QtWidgets import QApplication
from core.database import DatabaseManager
from ui.main_window import AgroClimateApp
from config.settings import Config
from config.security_config import SecurityConfig
from security.ai_security_guard import AISecurityGuard
from ui.dialogs.login_dialog import LoginDialog

def exception_handler(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    
    error_msg = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    SECURITY.log_event(f"CRITICAL ERROR: {error_msg}", "CRITICAL")
    
    error_dialog = QMessageBox()
    error_dialog.setIcon(QMessageBox.Icon.Critical)
    error_dialog.setWindowTitle("Критическая ошибка")
    error_dialog.setText("Произошла критическая ошибка в приложении.")
    error_dialog.setDetailedText(error_msg)
    error_dialog.setStandardButtons(QMessageBox.StandardButton.Ok)
    error_dialog.exec()
    
    sys.exit(1)

def handle_signal(signum, frame):
    signals = {
        signal.SIGINT: "SIGINT (Ctrl+C)",
        signal.SIGTERM: "SIGTERM",
    }
    
    SECURITY.log_event(f"Received signal: {signals.get(signum, f'Unknown ({signum})')}", "WARNING")
    QApplication.instance().quit()

# viatkino_agro_analyst/main.py
import sys
from core.logging import AppLogger
from core.database import DatabaseManager
from ui.main_window import AgroClimateApp
# ... другие импорты ...

def main():
    # Инициализация системы логирования
    logger = AppLogger(log_dir="logs", app_name="viatkino_agro_analyst")
    logger.log_application("Starting application initialization")
    
    try:
        # Инициализация базы данных
        logger.log_application("Initializing database")
        db_manager = DatabaseManager()
        
        # Инициализация GUI
        logger.log_application("Creating main application window")
        app = QApplication(sys.argv)
        window = AgroClimateApp(db_manager, logger)
        window.show()
        
        logger.log_application("Application started successfully")
        sys.exit(app.exec())
        
    except Exception as e:
        logger.log_application(f"Critical error during startup: {str(e)}", "critical")
        sys.exit(1)

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    # Инициализация конфигурации
    CONFIG = Config()
    SECURITY_CONFIG = SecurityConfig()
    
    # Настройка обработки исключений
    sys.excepthook = exception_handler
    
    if hasattr(signal, 'SIGINT'):
        signal.signal(signal.SIGINT, handle_signal)
    if hasattr(signal, 'SIGTERM'):
        signal.signal(signal.SIGTERM, handle_signal)
    
    app = QApplication(sys.argv)
    
    # Инициализация базы данных
    db_manager = DatabaseManager(CONFIG)
    
    # Аутентификация пользователя
    login_dialog = LoginDialog(db_manager)
    if login_dialog.exec() != QDialog.DialogCode.Accepted:
        sys.exit(0)
    
    # Создание главного окна
    window = AgroClimateApp(
        username=login_dialog.username,
        role=login_dialog.user_role,
        db_manager=db_manager,
        config=CONFIG,
        security_config=SECURITY_CONFIG
    )
    
    # Запуск системы безопасности
    security_guard = AISecurityGuard(SECURITY_CONFIG)
    security_guard.start()
    
    window.show()
    sys.exit(app.exec())

# main.py (дополнение)
from resources.icons.icon_manager import IconManager
from resources.translations.translation_manager import TranslationManager
from resources.geo_data.geo_manager import GeoManager

class AgroClimateApp(QMainWindow):
    def __init__(self, username, role, db_manager):
        # ...
        self.translation_manager = TranslationManager(CONFIG.current_lang)
        self.geo_manager = GeoManager()
        
        # Загрузка геоданных
        self.agro_zones = self.geo_manager.load_agro_zones(
            "resources/geo_data/agro_zones.geojson"
        )
        self.crop_suitability = self.geo_manager.load_crop_suitability(
            "resources/geo_data/crop_suitability.json"
        )
        
        # Настройка иконок
        self.setWindowIcon(IconManager.get_app_icon())
        self.tabs.setTabIcon(0, IconManager.get_climate_icon())
        self.tabs.setTabIcon(2, IconManager.get_analytics_icon())
    
    def tr(self, key: str) -> str:
        """Shortcut for translation"""
        return self.translation_manager.tr(key)
    
    def check_crop_suitability(self):
        crop = self.pred_crop.currentText()
        climate_data = self.get_current_climate_data()
        
        suitable, message = self.geo_manager.check_crop_suitability(
            crop, climate_data, self.crop_suitability
        )
        
        # Показать результат пользователю
        # ...
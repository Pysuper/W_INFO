import environ
from utils.log_theme import *

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path("wow")

env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True)
if READ_DOT_ENV_FILE:
    env.read_env(str(ROOT_DIR.path(".env")))

DEBUG = env.bool("DJANGO_DEBUG", False)
TIME_ZONE = "Asia/Shanghai"
LANGUAGE_CODE = "en-us"
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = [str(ROOT_DIR.path("locale"))]

# 数据库连接
DATABASES = {
    "default": env.db("DATABASE_URL", default="postgres:///wow")
}

# 是否将HTTP请求中对数据库的操作封装成事务
DATABASES["default"]["ATOMIC_REQUESTS"] = True

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# 将三个APP相加
DJANGO_APPS = [
    # "simpleui",  # 配置后台站点
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.admin",
    "django.forms",
]
THIRD_PARTY_APPS = [
    "crispy_forms",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.weixin",   # 配置微信登录
    "django_celery_beat",
    # "rest_framework",
    # "rest_framework.authtoken",
    "corsheaders",
    "sorl.thumbnail",
]
LOCAL_APPS = [
    "wow.users.apps.UsersConfig",
    "wow.item.apps.ItemConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# 更改查找组件模板的顺序，先自定义的模板，然后是系统默认的模板
FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

MIGRATION_MODULES = {"sites": "wow.contrib.sites.migrations"}

# 认证功能
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

AUTH_USER_MODEL = "users.User"
LOGIN_REDIRECT_URL = "users:redirect"
LOGIN_URL = "account_login"

# 加密算法
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

# 密码校验
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# 中间件
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# 静态文件配置
STATIC_ROOT = str(ROOT_DIR("staticfiles"))
STATIC_URL = "/static/"
STATICFILES_DIRS = [str(APPS_DIR("static"))]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_ROOT = str(APPS_DIR("media"))
MEDIA_URL = "/media/"

# 模板文件的配置
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(APPS_DIR("templates"))],
        "OPTIONS": {
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

# FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

CRISPY_TEMPLATE_PACK = "bootstrap4"

FIXTURE_DIRS = (str(APPS_DIR.path("fixtures")),)

# 安全配置
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = False  # 是否允许HTTP获取CSRFToken
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

# Email==> env()--在.env文件中定义
EMAIL_BACKEND = env("DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend")
EMAIL_HOST = env("DJANGO_EMAIL_HOST")
EMAIL_USE_SSL = env("DJANGO_EMAIL_USE_SSL", default=True)
EMAIL_PORT = env("DJANGO_EMAIL_PORT", default=465)
EMAIL_HOST_USER = env("DJANGO_EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("DJANGO_EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = env("DJANGO_DEFAULT_FROM_EMAIL")
EMAIL_TIMEOUT = 5

# Admin配置
ADMIN_URL = "admin/"
ADMINS = [("""zheng""", "zheng@example.com")]
MANAGERS = ADMINS

# Log
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
    'formatters': {  # 日志信息显示的格式
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s] %(message)s'
        },
    },
    'filters': {  # 对日志进行过滤
        'require_debug_true': {  # django在debug模式下才输出日志
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {  # 日志处理方法
        'console': {  # 向终端中输出日志
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {  # 日志器
        'django': {  # 定义了一个名为django的日志器
            'handlers': ['console'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'INFO',  # 日志器接收的最低日志级别
        },
    }
}

# Celery
# INSTALLED_APPS += ['wow.taskapp.celery.CeleryAppConfig']
if USE_TZ:
    CELERY_TIMEZONE = TIME_ZONE
CELERY_BROKER_URL = env("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND")
CELERY_ACCEPT_CONTENT = ["json", "msgpack"]  # msgpack-> celery序列化和反序列化的数据格式
CELERY_TASK_SERIALIZER = "msgpack"  # 序列化和反序列化的数据格式，二进制的json序列化方案
CELERY_RESULT_SERIALIZER = "json"  # 读取任务结果，一般性能不高，所以使用可读性更好的json
CELERY_TASK_TIME_LIMIT = 5 * 60  # 单个任务最大运行时间
CELERY_TASK_SOFT_TIME_LIMIT = 60  # 任务的软时间限制，超时后SoftTimeLimitExceeded异常会被抛出
# CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"


# django-allauth
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_ADAPTER = "wow.users.adapters.AccountAdapter"
SOCIALACCOUNT_ADAPTER = "wow.users.adapters.SocialAccountAdapter"

# django-compressor
INSTALLED_APPS += ["compressor"]
STATICFILES_FINDERS += ["compressor.finders.CompressorFinder"]

# django-rest-framework
# REST_FRAMEWORK = {
#     "DEFAULT_AUTHENTICATION_CLASSES": (
#         "rest_framework.authentication.SessionAuthentication",
#         "rest_framework.authentication.TokenAuthentication",
#     ),
#     "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
# }

# django-cors-headers
CORS_URLS_REGEX = r"^/api/.*$"

# ------------------------------------------------------------------------------


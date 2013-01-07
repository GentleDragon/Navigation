// The following ifdef block is the standard way of creating macros which make exporting 
// from a DLL simpler. All files within this DLL are compiled with the CONFIGMANAGER_EXPORTS
// symbol defined on the command line. This symbol should not be defined on any project
// that uses this DLL. This way any other project whose source files include this file see 
// CONFIGMANAGER_API functions as being imported from a DLL, whereas this DLL sees symbols
// defined with this macro as being exported.
#ifdef CONFIGMANAGER_EXPORTS
#define CONFIGMANAGER_API __declspec(dllexport)
#else
#define CONFIGMANAGER_API __declspec(dllimport)
#endif

// This class is exported from the ConfigManager.dll
class CONFIGMANAGER_API CConfigManager {
public:
	CConfigManager(void);
	// TODO: add your methods here.
};

extern CONFIGMANAGER_API int nConfigManager;

CONFIGMANAGER_API int fnConfigManager(void);
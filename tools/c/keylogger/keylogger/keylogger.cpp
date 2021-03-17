// keylogger.cpp : Defines the entry point for the DLL application.
#include "pch.h"
// https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setwindowshookexa
// https://docs.microsoft.com/en-us/previous-versions/windows/desktop/legacy/ms644986(v=vs.85)
// https://docs.microsoft.com/en-us/previous-versions/windows/desktop/legacy/ms644985(v=vs.85)
// https://docs.microsoft.com/ko-kr/windows/win32/api/winuser/nf-winuser-getasynckeystate?redirectedfrom=MSDN
// https://docs.microsoft.com/en-us/windows/win32/dlls/dllmain
// 

BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
                     )
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}


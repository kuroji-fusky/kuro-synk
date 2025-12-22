function synk {
  if (!(Get-Command -Name "py" -ErrorAction SilentlyContinue)) {
    Write-Error "Python not installed dummy"
    return 1
  }

  py kuro-synk.py --local-only
}

Export-ModuleMember -Function synk
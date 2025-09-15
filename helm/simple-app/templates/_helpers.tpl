{{/* Helpers for simple-app chart */}}
{{- define "simple-app.name" -}}
{{- .Chart.Name -}}
{{- end -}}

{{- define "simple-app.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}


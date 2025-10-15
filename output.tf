output "api_invoke_url" {
  value = "${aws_api_gateway_rest_api.api.execution_arn}/item"
  description = "Invoke URL for API Gateway"
}

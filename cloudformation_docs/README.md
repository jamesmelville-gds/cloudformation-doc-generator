# cloudformation_docs/template
## Description
Enable Guard Duty for every region in your account

### Parameters
The list of parameters for this template:
| Parameter        | Type   | Default   | Description |
|------------------|--------|-----------|-------------|
| AssumableOrgRoleArn | String |  |  |
| TargetOU | String |  |  |
| SpokeIAMPath | String | /guardduty-enabler/ |  |
| SpokeIAMRole | String | EnablerFunctionRole |  |
| ScheduleExpression | String | None | Cron or rate expressions to pass through to an AWS::Events::Rule <br> |

### Resources
The list of resources this template creates:
| Resource         | Type   |
|------------------|--------|
| EnablerFunctionRole | AWS::IAM::Role |
| EnablerFunction | AWS::Serverless::Function |
| EnablerFunctionCallerRole | AWS::IAM::Role |
| EnablerFunctionCusomResource | AWS::Serverless::Function |
| EnablerFunctionScheduler | AWS::Serverless::Function |
| SchedulingRule | AWS::Events::Rule |
| PermissionForEventsToInvokeLambda | AWS::Lambda::Permission |
| Enable | Custom::CustomResource |

### Outputs
The list of outputs this template exposes:
| Output           | Description   |
|------------------|---------------|
| PermissionForEventsToInvokeLambda | Some description about PermissionForEventsToInvokeLambda <br> |

// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Blueprint/UserWidget.h"
#include "APython_UI.generated.h"

/**
 * 
 */
UCLASS()
class EMOTION_PROJECT_C_2_API UAPython_UI : public UUserWidget
{
	GENERATED_BODY()
	
	public:
		UPROPERTY(BlueprintReadWrite, VisibleAnywhere, Category = "Python")
			FString DisplayText;

		UFUNCTION(BlueprintCallable, Category = "Widgets|Python")
			FString GetDisplayText();
	
};

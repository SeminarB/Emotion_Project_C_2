// Fill out your copyright notice in the Description page of Project Settings.

using UnrealBuildTool;
using System.Collections.Generic;

public class Emotion_Project_C_2Target : TargetRules
{
	public Emotion_Project_C_2Target(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Game;

		ExtraModuleNames.AddRange( new string[] { "Emotion_Project_C_2" } );
	}
}
